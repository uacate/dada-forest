from django.core.management.base import BaseCommand
from pathlib import Path
import requests
import json
from apps.catalogapp.models import Document

BASE_DIR = Path(__file__).resolve().parent


class Command(BaseCommand):
    help = "Load data from urls"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass


    def handle(self, *args, **options):
        print("Loading seed documents from test data.")

        with open(f"{BASE_DIR}/seed_data.json", "r") as f:
            data = json.load(f)
            for item in data:
                if item:
                    url = item["url"]
                    req = requests.get(url).json()
                    if req:
                        identifier = req["identifier"]
                        description = req["description"]
                        doc = Document(
                            identifier=identifier, url=url, description=description
                        )
                        doc.save()
