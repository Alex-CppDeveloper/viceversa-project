from django.shortcuts import render

def page_home(request):
	return render(request, 'indexHome.html')