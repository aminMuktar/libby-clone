from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.


def redirect_view(request):
    if request.user.is_authenticated:
        return redirect("/graphql")
    else:
        return redirect("/api")
