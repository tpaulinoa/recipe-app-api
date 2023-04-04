"""
Django commands to wait for database to be available
"""

import time
import csv
import argparse

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.db import IntegrityError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-d', '--doc_org_ids', nargs='+', type=str, help='List of doc ids and org ids')
        parser.add_argument('-f', '--csv_file', nargs='?', type=argparse.FileType('r'), help='List of doc ids and org ids')

    def handle(self, *args, **options):
        self.stdout.write("Doing some stuff...")

        documents = []
        for doc_org_ids in options['doc_org_ids']:
            time.sleep(1)
            try:
                doc_id, org_id = doc_org_ids.split(",")
                # doc = Document(document_uuid=doc_id, organization_uuid=org_id)
                # doc.save()
                self.stdout.write("created... doc_id=" + doc_id + " | org_id=" + org_id)
            except ValueError:
                self.stdout.write(f"invalid value = {doc_org_ids}")
            except IntegrityError:
                self.stdout.write(f"Document = {doc_id} already exists")
        # try:
        #     docs_created = Document.objects.bulk_create(documents, ignore_conflicts=True)
        #     #for doc in docs_created:
        #     #    self.stdout.write(f"id={doc.pk} | doc_uuid={doc.document_uuid} | purchased_at={doc.purchased_at}")
        #     for doc in documents:
        #         self.stdout.write(f"id={doc.pk} | doc_uuid={doc.document_uuid} | purchased_at={doc.purchased_at}")
        # except IntegrityError:
        #     for doc in documents:
        #         if doc.pk is None:
        #             self.stdout.write(f"document_id = {doc.document_uuid} already exists")

        # with options['csv_file'] as csvfile:
        #      reader = csv.DictReader(csvfile)
        #      for row in reader:
        #          self.stdout.write("doc_id=" + row["doc_id"] + " | org_id=" + row["org_id"])

        self.stdout.write("Finished!")
