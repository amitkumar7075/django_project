#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import Step1Form, Step2Form, Step3Form
from .models import UserProfile

def step1_view(request):
    if request.method == 'POST':
        form = Step1Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            request.session['user_id'] = user.id
            return redirect('step3_view')
    else:
        form = Step1Form()
    return render(request, 'step1.html', {'form': form})

def step2_view(request):
    user_id = request.session.get('user_id')
    user = UserProfile.objects.get(id=user_id)
    if request.method == 'POST':
        form = Step2Form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('step3_view')
    else:
        form = Step2Form(instance=user)
    return render(request, 'step2.html', {'form': form})

def step3_view(request):
    user_id = request.session.get('user_id')
    user = UserProfile.objects.get(id=user_id)
    if request.method == 'POST':
        form = Step3Form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('success_view')
    else:
        form = Step3Form(instance=user)
    return render(request, 'step3.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')
