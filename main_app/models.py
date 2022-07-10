from audioop import reverse
from django.db import models

# Create your models here.
class Germ(models.Model):
    common_name = models.CharField(max_length=100)
    germ_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    mode_of_trans = models.CharField(max_length=100)


    def __str__(self):
        return self.common_name

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={'germ_id': self.id})

    










# g = Germ(common_name='COVID-19', germ_name="SARS-CoV-2", type="Virus", mode_of_trans="Contact/Droplet")






    #   self.common_name = common_name
    #     self.germ_name = germ_name
    #     self.type = type
    #     self.mode_of_trans = mode_of_trans
