
from django.shortcuts import render
from .models import place
# Create your views here.
def demo(request):
    #name="India"
    obj=place.objects.all()
    return render(request,"home.html",{'result':obj})


#def operations(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #add=x+y
    #sub=x-y
    #mul=x*y
    #div=x/y
    #return render(request, "result.html", {"addition":add,"subtract":sub,"multiply":mul,"division":div})
#def subtraction(request):
     #x = int(request.GET['num1'])
     #y = int(request.GET['num2'])
     #a=x-y
     #return render(request, "result.html", {'sub':a})
#def multiplication(request):
    #x = int(request.GET['num1'])
    #y = int(request.GET['num2'])
    #b=x*y
    #return render(request, "result.html", {'mul':b})
#def division(request):
    #x = int(request.GET['num1'])
    #y = int(request.GET['num2'])
    #c=x/y
    #return render(request, "result.html", {'div': c})

#def about(request):
    #return render(request,"about.html")

#def contact(request):
  #return HttpResponse("hello iam contact")

#def detail(request):
  #return HttpResponse("details please")

#def thanks(request):
    #return render(request,"thanks.html")
