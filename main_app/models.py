from django.urls import reverse
from django.db import models

# A tuple of 2-tuples
TREATMENTS = (
    ( 'M', 'Medication' ),
    ( 'D', 'Diet' ),
    ( 'S', 'Supplements'),
    ( 'L', 'Lifestyle Changes')
)

VAX_PREV = (
    ('Y', 'Yes'),
    ('N', 'No')
)

# Create your models here.
class Germ(models.Model):
    common_name = models.CharField(max_length=100)
    germ_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    mode_of_trans = models.CharField(max_length=100)
    # Add many to many relationship

    def __str__(self):
        return self.common_name

    def get_absolute_url(self):
       return reverse("detail", kwargs={'germ_id': 
       self.id})
        


class Treatment(models.Model):
    tx = models.CharField(max_length=200,
        #add the choices field option
        choices=TREATMENTS, 
        # set the default value for treatment to be Medication
        default=TREATMENTS[0][0])
    vax_prevent = models.CharField(max_length=1,
        choices=VAX_PREV,
        default=VAX_PREV[1][0])
    
    # Create a germ_id FK
    germ = models.ForeignKey('Germ', on_delete=models.CASCADE)

    #basically a console.log
    # def __str__(self):
    #     # return f"{% treatment.tx.get %}"
    #     return f"{self.get_treatment_display()}"
   











# g = Germ(common_name='COVID-19', germ_name="SARS-CoV-2", type="Virus", mode_of_trans="Contact/Droplet")

    #   self.common_name = common_name
    #     self.germ_name = germ_name
    #     self.type = type
    #     self.mode_of_trans = mode_of_trans
