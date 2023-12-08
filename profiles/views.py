from django.shortcuts import render
from profiles.forms import ProfileForm

# Create your views here.
def add_profile(request):
    profile_form = ProfileForm()
    
    return render(request, 'add_profile.html', {'form': profile_form})