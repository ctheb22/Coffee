from django.db import models


class RoastLevel(models.Model):
    level_name = models.CharField(max_length=100)
    def __str__(self):
        return self.level_name


class Coffee(models.Model):
    coffee_name = models.CharField(max_length=200)
    suggested_roast = models.ForeignKey(RoastLevel, on_delete=models.CASCADE)
    def __str__(self):
        return self.coffee_name


class Roast(models.Model):
    roast_number = models.IntegerField(unique=True)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    roast_level = models.ForeignKey(RoastLevel, on_delete=models.CASCADE)
    date = models.DateTimeField('Roast Date')
    notes = models.CharField(max_length=1000)
    dev_percent = models.IntegerField()
    weight_percent = models.IntegerField()
    def __str__(self):
        return self.roast_number


class RoastDataPoints(models.Model):
    roast = models.ForeignKey(Roast, on_delete=models.CASCADE)
    env_temp = models.IntegerField()
    exh_temp = models.IntegerField()
    time = models.TimeField()
    note = models.CharField(max_length=500)
    def __str__(self):
        return self.roast + ' : ' + self.time


class Reviews(models.Model):
    roast = models.ForeignKey(Roast, on_delete=models.CASCADE)
    notes = models.charField(max_length=1500)
    reviewer = models.charField(max_length=50)
    rating = models.FloatField()