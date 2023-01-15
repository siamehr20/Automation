from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.html import format_html
from django.views import View
from Employee.forms import RegisterForm, LoginForm, CompleteRegistrationForm
from Employee.models import Employee


# Create your views here.

def dashboard(request):
    return render(request, './Employee/dashboard.html')


def register(request):
    return render(request, "Employee/page-register.html")


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()

        context = {
            'register_form': register_form,
            # 'personal_id':0,
            'user_id': 0
        }
        return render(request, "Employee/page-register.html", context)

    def post(self, request):
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            print(register_form.clean())

            username_input = register_form.cleaned_data['username']
            username = Employee.objects.filter(username__iexact=username_input)
            username_existance = username.exists()

            user_email_input = register_form.cleaned_data['email']
            user_email = Employee.objects.filter(email__exact=user_email_input)
            user_email_existance = user_email.exists()

            if user_email_existance and user_email_existance:
                register_form.add_error(field='email', error='ایمیل وارد شده در سیستم موجود میباشد..!')
                register_form.add_error(field='username', error='نام کاربری وارد شده در سیستم موجود میباشد..!')
            elif username_existance:
                register_form.add_error(field='username', error='نام کاربری وارد شده در سیستم موجود میباشد..!')
            elif user_email_existance:
                register_form.add_error(field='email', error='ایمیل وارد شده در سیستم موجود میباشد..!')

            else:
                new_user = Employee(
                    username=username,
                    email=user_email,
                    personal_id=Employee.generate_personal_id(),
                    account_activation_url=get_random_string(45)
                )
                new_user.set_password(
                    raw_password=register_form.cleaned_data['password']
                )
                new_user.pas
                # new_user.save()
                # self.personal_id = 12345
                # { 'personal_id': self.personal_id }

                return redirect(reverse('complete_signup-page', kwargs={'id': new_user.personal_id}))
            context = {
                'register_form': register_form,

            }
        return render(request, "Employee/page-register.html", context)


class CompleteRegistrationView(View):
    # user_pk = RegisterView.
    def get(self, request, personal_id):
        complete_form = CompleteRegistrationForm()

        context = {
            'title': 'تکمیل فرم ثبت نام',
            'complete_form': complete_form,
            'span_tag': format_html('<span class="text-danger">*</span>'),
            'user_id': personal_id
        }
        return render(request, "Employee/complete-signup-form.html", context)

    def post(self, request, personal_id):
        complete_form = CompleteRegistrationForm(request.POST)
        register_form = RegisterForm(request.POST)
        if complete_form.is_valid():
            # user_object = Employee.objects.filter(
            #     username__iexact=register_form.cleaned_data.get('username')
            # )
            complete_form_data = complete_form.cleaned_data
            register_form_data = register_form.cleaned_data
            user = Employee(
                username=register_form_data['username'],
                email=register_form_data['email'],
                first_name=complete_form_data['firstname'],
                last_name=complete_form_data['last_name'],
                national_id=complete_form_data['national_id'],
                birthday=complete_form_data['birthday'],
                gender=complete_form_data['gender'],
                phone_number=complete_form_data['phone_number']
            )
            user.set_password(
                raw_password=register_form.cleaned_data['password']
            )
            user.save()
            return redirect(reverse('login_page'))

            # Employee.objects.create(
            #     first_name=complete_form_data['firstname'],
            #     last_name=complete_form_data['last_name'],
            #     national_id=complete_form_data['national_id'],
            #     birthday=complete_form_data['birthday'],
            #     gender=complete_form_data['gender'],
            #     phone_number=complete_form_data['phone_number']
            # )
        context = {'complete_form': complete_form,

                   }

        return render(request, './Employee/complete-signup-form.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, "Employee/page-login.html", context)

    def post(self, request):
        return render(request, "Employee/page-login.html")
