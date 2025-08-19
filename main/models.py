from django.db import models

# Create your models here.

class EntryModel(models.Model):
    user = models.CharField()
    value = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    source = models.CharField(max_length=100)
    borrowed = models.BooleanField()



    def __str__(self):
        return str(self.value) + " " + str(self.date) + " " + self.source + " " + str(self.borrowed)


class TotalValues(models.Model):
    user = models.CharField()
    total = models.IntegerField()
    thisMonth = models.IntegerField()

    def __str__(self):
        return str(self.user) + " " + str(self.total) + " " + str(self.thisMonth)
