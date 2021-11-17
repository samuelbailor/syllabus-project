from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from faculty_profile.models import Profile
from .forms import EditProfileForm


def index(request, user_id):
    profiles = Profile.objects.filter()
    return render(request, 'faculty_profile/index.html', context={'profiles': profiles})


def edit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/add/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EditProfileForm()

    return render(request, 'faculty_profile/edit.html', {'form': form})


def syllabus(request):
    return HttpResponse('View will be connected to the syllabus app later')


def add(request):
    # if ID from form POST is the same as an ID that is already in the database, the existing entry will be modified
    # if ID is new, a new entry will be created
    profile_id = request.POST['ID']
    location = request.POST['location']
    phone = request.POST['phone']
    hours = request.POST['hours']
    profile_obj = Profile(ID=profile_id, location=location, phone=phone, hours=hours)
    profile_obj.save()
    return HttpResponseRedirect(reverse('faculty_profile:index'))
