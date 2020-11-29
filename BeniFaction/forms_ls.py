from django.contrib.auth.forms import AuthenticationForm, authenticate
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, reverse
from django.http import request


def login_per(request):
    if request.user.is_authenticated:
        return redirect('/donate')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/donate/')
                else:
                    er = "Invalid Username or Password. Try again"
                    return render(request, "BeniFaction/log1n_user.html",{
                        "form": form,
                        "error" : er})
            else:
                er = "Invalid Username or Password. Try again"
                return render(request, "BeniFaction/log1n_user.html",{
                    "form": form,
                    "error" : er})

        form = AuthenticationForm()
        return render(request,
                    template_name = "BeniFaction/log1n_user.html",
                    context={"form":form})
        
def donate_form(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST['email']
        aff = request.POST['aff']
        valid = request.POST.cleaned_data['validid']
        don_drive = request.POST.cleaned_data['don_drive_title']
        don_desc = request.POST['don_drive_desc']
        amount = request.POST['amount']
        doc_in = request.POST['doc_in']

    return render(request, "BeniFaction/donate_form.html", {
        }) 
def reques_form(request):
    if request.method == "POST":
        

