from django.apps import AppConfig


class ViewflowConfig(AppConfig):
    """Default Viewflow application config."""

    icon = '<i class="material-icons">assignment</i>'
    name = 'viewflow'
    verbose_name = 'Workflow'
    default_auto_field = 'django.db.models.AutoField'
