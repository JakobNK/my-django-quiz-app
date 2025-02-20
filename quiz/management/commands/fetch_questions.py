import requests
import html
from django.core.management.base import BaseCommand
from django.utils import timezone
from quiz.models import Question  # Make sure this matches your app's name

class Command(BaseCommand):
    help = "Fetches daily quiz questions from OpenTDB API"

    def handle(self, *args, **kwargs):
        categories = [9, 10, 11, 12, 13, 14, 15]  # Example categories
        category = categories[timezone.now().day % len(categories)]  # Rotate daily

        url = f"https://opentdb.com/api.php?amount=10&category={category}&difficulty=easy&type=multiple"
        response = requests.get(url)
        data = response.json()

        for item in data["results"]:
            Question.objects.create(
                question_category = html.unescape(item["category"]),
                question_text=html.unescape(item["question"]),
                correct_answer=html.unescape(item["correct_answer"]),
                incorrect_answers=[html.unescape(ans) for ans in item["incorrect_answers"]],
            )

        self.stdout.write(self.style.SUCCESS(f"Fetched questions for category {category}"))