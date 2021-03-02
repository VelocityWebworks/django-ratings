from django.core.management.base import BaseCommand, CommandError

from djangoratings.models import SimilarUser

class Command(BaseCommand):
    def handle_noargs(self, **options):
        SimilarUser.objects.update_recommendations()
