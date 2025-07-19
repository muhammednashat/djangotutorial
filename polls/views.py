from django.http import HttpResponse

def index(request):  
    return HttpResponse(
        f"  {request}   Welcom,      to mysite from qena,        I did it ya wlaad ellaeba,         I am not weak  I can speak english very will ,         beteer thatn                         amirican english                           "
    ) 
