from django.http import HttpResponse
from django.utils import timezone

from .models import User


def index(request):
    response_text = ""
    for i in range(100):
        user = User(username=f"spellChecker-{i}", password="123",
                       email=f"user{i}@gmail.com", datetime_created=timezone.now())
        user.save()

    users = User.objects.all()

    for user in users:
        response_text += user.username + "\n"

    return HttpResponse(response_text)
