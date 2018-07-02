from django.shortcuts import render

# Create your views here.
def view_renderer(request):
	context = {
	"msg": "Hello World"
	}
	return render(request, "homepage.html", context)