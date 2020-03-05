from django.shortcuts import render,redirect
from django.http import HttpResponse

from demo1.forms import MyForm
from demo1.models import Truth
# Create your views here.
def demo1(request):
	pass
def form(request):
	return render(request,'form.html')
	return render(request,'show.html')
	if request.method == 'GET':
		name = request.GET['name']
		email = request.GET['email']
		mobile = request.GET['mob']
		salary = request.GET['sal']
		data = [name,email,mobile,salary]
		return HttpResponse(data)
def adddata(request):
	if request.method == 'GET':
		form = MyForm(request.GET)
		if form.is_valid():
			form.save()
			return redirect('/getdata/')
		else:
			form = MyForm()
	return render(request,'form.html',{'form':form})

def getdata(request):
	data = Truth.objects.all()
	return render(request,'show.html',{'data':data})

def delete(request,id):
	#return HttpResponse(id)
	data = Truth.object.get(id=id)
	data.delete()
	return redirect('/getdata/')

def getdataforedit(request,id):
	data = Truth.objects.get(id=id)
	return render(request,'editdata.html',{'data':data})

def update(request,id):
	if request.method=="GET":
		emp = Truth.objects.get(id=id)
		form = MyForm(request.GET,instance=emp)
		if form.is_valid():
			try:
				form.save()
				return redirect('/getdata')
			except:
				pass
			else:
				form = MyForm()
				return render(request,"editdata.html",{'form':form})




		



