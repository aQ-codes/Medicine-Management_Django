from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Medicine
from .forms import MedicineForm , CreateuserForm
import json

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        
        form = CreateuserForm()

        if request.method == 'POST':
            form = CreateuserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')#get username without other attributes
                messages.success(request, 'Account was created for '+ user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        #check if user in database
            user = authenticate(request, username=username, password= password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password incorrect')

        context = {}
        return render(request, 'login.html',context)


def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):  
  
    medicines = Medicine.objects.order_by('-date_created')[:10]               
    
    ayur_medicines = Medicine.objects.filter(category = 'Ayurveda').count()
    allo_medicines = Medicine.objects.filter(category = 'Allopathy').count()
    homeo_medicines = Medicine.objects.filter(category = 'Homeopathy').count()

    total_medicines = Medicine.objects.all().count()

    form = MedicineForm()
    context = {'medicines': medicines,'total_medicines': total_medicines, 'homeo_medicines':homeo_medicines ,'allo_medicines':allo_medicines ,'ayur_medicines':ayur_medicines, 'form':form} 

    return render(request, 'dashboard.html', context)


@login_required(login_url='login') 
def createMed(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    else:
        form = MedicineForm()

    return render(request,'add.html',{'form':form})


@login_required(login_url='login')
def updateMed(request, id):
    med = Medicine.objects.get(pk=id)
    form = MedicineForm(instance = med)  

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance = med  )
        if form.is_valid():
            form.save()  
            return redirect('/') 
        
    context ={'form':form}
    return render(request, 'update.html', context)

@login_required(login_url='login')
def deleteMed(request, id):
    med = Medicine.objects.get(pk=id)
    if request.method == "POST":
        med.delete()
        return redirect('/')

    context = {'medicine':med}
    return render(request, 'delete.html', context)

@login_required(login_url='login')
def listMed(request):     

    search_item = request.GET.get('search', '')
    if search_item :
        medicines = Medicine.objects.filter(name__istartswith = search_item)  
    else:
          medicines = Medicine.objects.all()   
    return render(request, 'medicines.html', {'medicines':medicines} ) 

@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText') #cconverting json to python dictionary and getting the searchtext key value
        medicines = Medicine.objects.filter(name__istartswith = search_str) #so this is a query set
        data = medicines.values() #dictionary list
        return JsonResponse(list(data), safe = False) #safe is false because jsonresponse only accept dictionaries by default.Here we need to pass list
       
@login_required(login_url='login')
def handling_404(request, exception):
    return render (request, 'dashboard.html', {})
