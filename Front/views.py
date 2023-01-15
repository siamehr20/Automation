from django.shortcuts import render

# Create your views here.





def show_title(request):
    return render(request, 'Front/app-profile.html', context={'title' : 'Nourad Automation'})
