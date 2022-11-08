from django.core.management import BaseCommand

from main.tasks import dummy, dramatiq_dummy


class Command(BaseCommand):
    help = "Run a task"

    def add_arguments(self, parser):
        parser.add_argument(
            "--fail",
            action="store_true",
            help="Fail the task",
        )
        parser.add_argument(
            "--dramatiq",
            action="store_true",
            help="Use dramatiq",
        )
        parser.add_argument(
            "--num",
            type=int,
            default=1,
        )

    def handle(self, *args, **options):
        for _ in range(options["num"]):
            if options["dramatiq"]:
                dramatiq_dummy.send(options["fail"])
            else:
                dummy.delay(fail=options["fail"])
            self.stdout.write(self.style.SUCCESS("Task started"))
