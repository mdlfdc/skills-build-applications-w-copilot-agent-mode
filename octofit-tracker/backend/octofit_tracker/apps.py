from django.apps import AppConfig
import logging

class OctofitTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'octofit_tracker'

    def ready(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.debug('OctofitTracker app is being loaded')
