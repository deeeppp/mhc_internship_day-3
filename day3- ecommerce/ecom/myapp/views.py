from django.shortcuts import render,get_object_or_404,redirect
from .models import Electronics,Fashion, Grocery

def electronic_list(request):
 elec=Electronics.objects.all()
 return render(request,"electronic_list.html" ,{"elec": elec})

def electronics_add(request):
 if request.method=='POST':
  DeviceName=request.POST.get('name')
  Color=request.POST.get('color')
  Brand=request.POST.get('brand')
  Price=request.POST.get('price')
  Electronics.objects.create(
   DeviceName=DeviceName,
   Color=Color,
   Brand=Brand,
   Price=Price
  )
  return redirect("electronic_list")
 return render(request,"elect_form.html")

def electronics_edit(request,pk):
 electronic=get_object_or_404(Electronics,pk=pk)
 if request.method=='POST':
  electronic.name=request.POST.get('name')
  electronic.color=request.POST.get('color')
  electronic.brand=request.POST.get('brand')
  electronic.price=request.POST.get('price')
  electronic.save()
  return redirect("electronic_list")
 return render(request,"elect_form.html",{"electronic":electronic})

def electronics_delete(request,pk):
 electronic=get_object_or_404(Electronics,pk=pk)
 if request.method=='POST':
  electronic.delete()
  return redirect("electronic_list")
 return render(request,"elect_del.html",{"electronic":electronic})

#Fachion
def fash_list(request):
 fash=Fashion.objects.all()
 return render(request,"fash_list.html" ,{"fash": fash})

def fash_add(request):
 if request.method=='POST':
  Name=request.POST.get('name')
  Color=request.POST.get('color')
  Brand=request.POST.get('brand')
  Price=request.POST.get('price')
  Fashion.objects.create(
   Name=Name,
   Color=Color,
   Brand=Brand,
   Price=Price
  )
  return redirect("fash_list")
 return render(request,"fash_form.html")

def fash_edit(request,pk):
 fash=get_object_or_404(Fashion,pk=pk)
 if request.method=='POST':
  fash.name=request.POST.get('name')
  fash.color=request.POST.get('color')
  fash.brand=request.POST.get('brand')
  fash.price=request.POST.get('price')
  fash.save()
  return redirect("fash_list")
 return render(request,"elect_form.html",{"fash":fash})

def fash_delete(request,pk):
 fash=get_object_or_404(Fashion,pk=pk)
 if request.method=='POST':
  fash.delete()
  return redirect("fash_list")
 return render(request,"elect_del.html",{"fash":fash})

#Grocery

def groc_list(request):
 groc=Grocery.objects.all()
 return render(request,"groc_list.html" ,{"groc": groc})

def groc_add(request):
 if request.method=='POST':
  Name=request.POST.get('name')
  Quantity=request.POST.get('quantity')
  Price=request.POST.get('price')
  Grocery.objects.create(
   Name=Name,
   Quantity=Quantity,
   Price=Price
  )
  return redirect("groc_list")
 return render(request,"groc_form.html")

def groc_edit(request,pk):
 groc=get_object_or_404(Grocery,pk=pk)
 if request.method=='POST':
  groc.name=request.POST.get('name')
  groc.color=request.POST.get('color')
  groc.brand=request.POST.get('brand')
  groc.price=request.POST.get('price')
  groc.save()
  return redirect("groc_list")
 return render(request,"elect_form.html",{"groc":groc})

def groc_delete(request,pk):
 groc=get_object_or_404(Grocery,pk=pk)
 if request.method=='POST':
  groc.delete()
  return redirect("groc_list")
 return render(request,"elect_del.html",{"groc":groc})