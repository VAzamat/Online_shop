from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print( f'{username} ({email},{message})')
    return render(request, 'dealer/index.html')
