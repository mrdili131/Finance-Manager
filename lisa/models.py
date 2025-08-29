from django.db import models
from users.models import User


action_type = [
    ('kirim','kirim'),
    ('chiqim','chiqim')
]

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Finance(models.Model):
    amount = models.DecimalField(default=0,decimal_places=0,max_digits=10)
    description = models.TextField(default="")
    type = models.CharField(choices=action_type,default='kirim',max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} | {self.type} | {self.amount}so\'m'