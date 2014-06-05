from django.db import models
from django.contrib.auth.models import User

class Column(models.Model):
	name = models.CharField(max_length=32)
	price = models.FloatField(default=0)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']

class Pop(models.Model):
	name = models.CharField(max_length=32)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']

class PopColumnRelation(models.Model):
	pop = models.ForeignKey(Pop)
	column = models.ForeignKey(Column)
	def __str__(self):
		return str(self.pop) + ' goes in ' + str(self.column)

class Filling(models.Model):
	pop = models.ForeignKey(Pop)
	column = models.ForeignKey(Column)
	time = models.DateTimeField(auto_now_add = True)
	amount = models.IntegerField(default=0)
	user = models.ForeignKey(User)
	was_empty = models.BooleanField(default=False)
	def __str__(self):
		return str(self.amount) + ' ' +  str(self.pop) + ' into ' + str(self.column)

class Stocking(models.Model):
	pop = models.ForeignKey(Pop)
	amount = models.IntegerField(default=0)
	price = models.FloatField(default=0)
	user = models.ForeignKey(User)
	was_empty = models.BooleanField(default=False)
	time = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.amount) + ' ' +  str(self.pop) + ' for ' + str(self.price)

