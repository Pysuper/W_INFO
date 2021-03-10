from django.db import models


class Items(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, verbose_name="ID")
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="名称")
    grade = models.CharField(max_length=50, null=True, blank=True, verbose_name="等级")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标")
    table = models.CharField(max_length=255, null=True, blank=True, verbose_name="Table")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)
        verbose_name_plural = verbose_name = "用户"
