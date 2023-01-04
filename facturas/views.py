from django.shortcuts import render
from facturas.models import Detalle_Factura

def factura(request):
    #return HttpResponse("Hola")
    productos = Detalle_Factura.objects.all()
    return render(request, "facturas/facturas.html", {'productos':Detalle_Factura})
