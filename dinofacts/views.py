from django.shortcuts import render
from datetime import datetime



# Create your views here.
def dino(request):
    return render(request,"dino.html")
 
def detail(request,pk):
    context={"pk":pk,}
    return render(request,"detail.html",context)
  

def show_dino(request, name):
    data = {
        "dinosaurs": [
            "Tyrannosaurus",
            "Stegosaurus",
            "Raptor",
            "Triceratops",
        ],
        "now": datetime.now(),
    }

    return render(request, name + ".html", data)
