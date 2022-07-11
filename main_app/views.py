
from django.shortcuts import render
from django.http import HttpResponse
from . models import Germ
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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



def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')     


def about(request):
    return render(request, 'about.html')

def germs_index(request):
    germs = Germ.objects.all()
    return render(request, "germs/index.html", {'germs': germs })

def germs_detail(request, germ_id):
    #get individual germ
    germ = Germ.objects.get(id=germ_id)
    # render template, pass it to the cat
    return render(request, 'germs/detail.html', { 'germ': germ})

class GermCreate(CreateView):
    model = Germ
    fields = '__all__'
    success_url = '/germs/'

class GermUpdate(UpdateView):
    model = Germ
    #Disallow the renaming of a germ by excluding the name field
    fields = ['common_name','type', 'mode_of_trans']

class GermDelete(DeleteView):
    model = Germ
    success_url = '/germs/'
