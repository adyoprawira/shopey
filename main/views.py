from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Shopey',
        'name' : "Adyo Arkan Prawira",
        'class' : 'KKI',
    }
    
    return render(request, "main.html", context)
