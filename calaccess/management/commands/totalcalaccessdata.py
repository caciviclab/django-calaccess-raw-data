from django.core.management.base import BaseCommand
from django.db.models.loading import get_models, get_app
from django.contrib.humanize.templatetags.humanize import intcomma


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        model_list = get_models(get_app("calaccess"))
        print "%s total database tables" % len(model_list)
        record_count = 0
        for m in model_list:
            record_count += m.objects.count()
        print "%s total database records" % intcomma(record_count)
