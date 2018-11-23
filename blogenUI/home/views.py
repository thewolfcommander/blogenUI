from django.shortcuts import render

# Create your views here.
def categories(request):
	context = {

	}
	return render(request, 'categories.html', context)

def details(request):
	context = {
	
	}
	return render(request, 'details.html', context)

def posts(request):
	context = {
	
	}
	return render(request, 'posts.html', context)

def profile(request):
	context = {
	
	}
	return render(request, 'profile.html', context)

def settings(request):
	context = {
	
	}
	return render(request, 'settings.html', context)

def users(request):
	context = {
	
	}
	return render(request, 'users.html', context)