from django.http import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


monthly_challenges = {
    "january": "eat no meat",
    "february": "walk for at least 20 min",
    "march": "learn django for 20 min",
    "april": "go for a run",
    "may": "eat no meat",
    "june": "walk for at least 20 min",
    "july": "learn django for 20 min",
    "august": "go for a run",
    "september": "eat no meat",
    "october": "walk for at least 20 min",
    "november": "learn django for 20 min",
    "december": None
}

# Create your views here.

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

        
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
        
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args = [redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
