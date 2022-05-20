from django.db import models
from login.models import User
# Create your models here.

class History(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    explicit_symptom = models.CharField(max_length=200)
    implicit_symptom = models.CharField(max_length=200)
    disease_tag = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
            # auto_now = Ture，字段保存时会自动保存当前时间，但要注意每次对其实例执行save()
            # 的时候都会将当前时间保存，也就是不能再手动给它存非当前时间的值。每一次执行修改等动作，时间保持当前的。而非首次的创建时间。
            #
            # auto_now_add = True，字段在实例第一次保存的时候会保存当前时间，不管你在这里是否对其赋值。但是之后的save()
            # 是可以手动赋值的。也就是新实例化一个model，想手动存其他时间，就需要对该实例save()
            # 之后赋值然后再save()。（保持首次创建的时间，后再对实例变动修改，这个值不会变化的）
    def __str__(self):
        return self.disease_tag

    class Meta:
        ordering = ['-date']
