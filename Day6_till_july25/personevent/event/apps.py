from django.apps import AppConfig


class EventConfig(AppConfig):
    name = 'event'

    def ready(self):
        print ("signals is available .. to use")
        import event.signals
