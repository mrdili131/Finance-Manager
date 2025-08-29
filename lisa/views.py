from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Finance, Category
from .forms import FinanceForm
from users.models import User

class IndexVew(LoginRequiredMixin,View):
    def get(self,request):
        categories = Category.objects.all()
        form = FinanceForm()
        return render(request,'index.html',{'form':form,'categories':categories})
    
    def post(self,request):
        categories = Category.objects.all()
        form = FinanceForm(request.POST)
        user = User.objects.get(id=request.user.id)
        print("post")
        if form.is_valid():
            print("valid")
            new_form = form.save(commit=False)
            new_form.user = request.user
            if form.cleaned_data["type"] == "kirim":
                user.balance += form.cleaned_data["amount"]
            elif form.cleaned_data["type"] == "chiqim":
                user.balance -= form.cleaned_data["amount"]
            user.save()
            new_form.save()
            return redirect('home')
        return render(request,'index.html',{'form':form,'categories':categories})
    
class ReportView(LoginRequiredMixin,View):
    def get(self,request):
        reports = Finance.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'actions.html',{'reports':reports})