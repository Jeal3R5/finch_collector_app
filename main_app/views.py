
from mimetypes import common_types
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Germ, Treatment, Symptom
from .forms import TreatmentForm


# class Germ:
#     def __init__(self, common_name, germ_name, type, mode_of_trans):
#         self.common_name = common_name
#         self.germ_name = germ_name
#         self.type = type
#         self.mode_of_trans = mode_of_trans

# germs = [
#     Germ('MRSA', 'Methicillin-Resistant Staphylococcus aureus', 'Bacteria', 'Contact'),
#     Germ('COVID-19', 'SARS-CoV-2', 'Virus', 'Droplet'),
#     Germ('C Auris', 'Candida auris', 'Fungi', 'Contact'),
#     Germ('Chagas Disease', 'Trypanosoma cruzi', 'Protozoa', 'Vectorborne' )
# ]


# S3_BASE_URL = "https://s3-us-west-1.amazonaws.com"
# BUCKET = 'germ-collector-jr-83'

class GermCreate(CreateView):
    model = Germ
    fields = [ 'common_name', 'germ_name', "type", 'mode_of_trans']
    success_url = '/germs/'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GermUpdate(UpdateView):
    model = Germ
    #Disallow the renaming of a germ by excluding the name field
    fields = ['common_name','type', 'mode_of_trans']

class GermDelete(DeleteView):
    model = Germ
    success_url = '/germs/'

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')     


def about(request):
    return render(request, 'about.html')

def germs_index(request):
    germs = Germ.objects.filter(user=request.user)
    return render(request, "germs/index.html", {'germs': germs })

def germs_detail(request, germ_id):
    #get individual germ
    germ = Germ.objects.get(id=germ_id)
    tx_form = TreatmentForm()
    # render template, pass it to the cat
    return render(request, 'germs/detail.html', {'germ':germ, 'tx_form': tx_form})

def add_treatment(request, germ_id):
    form = TreatmentForm(request.POST)
    if form.is_valid():
        new_tx = form.save(commit=False)
        new_tx.germ_id = germ_id
        new_tx.save()
    return redirect('detail', germ_id)



class SymptomCreate(CreateView):
    model = Symptom
    fields = '__all__'


class SymptomUpdate(UpdateView):
    model = Symptom
    #Disallow the renaming of a germ by excluding the name field
    fields = ['symptom']

class SymptomDelete(DeleteView):
    model = Symptom
    success_url = '/symptoms/'

class SymptomList(ListView):
    model = Symptom

class SymptomDetail(DetailView):
    model = Symptom

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = "Invalid sign up - please try again"
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)