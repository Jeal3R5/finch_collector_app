from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


class Germ:
    def __init__(self, common_name, germ_name, type, mode_of_trans):
        self.common_name = common_name
        self.germ_name = germ_name
        self.type = type
        self.mode_of_trans = mode_of_trans

germs = [
    Germ('MRSA', 'Methicillin-Resistant Staphylococcus aureus', 'Bacteria', 'Contact'),
    Germ('COVID-19', 'SARS-CoV-2', 'Virus', 'Droplet'),
    Germ('C Auris', 'Candida auris', 'Fungi', 'Contact'),
    Germ('Chagas Disease', 'Trypanosoma cruzi', 'Protozoa', 'Vectorborne' )
]



def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')      #This is like res.send in express


def about(request):
    return render(request, 'about.html')

def germs_index(request):
    return render(request, 'germs/index.html', { 'germs': germs })