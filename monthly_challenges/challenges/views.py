from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
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
    "december": "go for a run"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
        
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args = [redirect_month]) # /challenge
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
