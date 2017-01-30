from django.core.management.base import BaseCommand, CommandError
from scraper.get_the_news import GetTheNews


class Command(BaseCommand):
    help = 'Run the scraper and store headlines in DB'

    def handle(self, *args, **options):
        control = GetTheNews()
        control.runScrapers()
