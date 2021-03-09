from django.contrib.auth.mixins import LoginRequiredMixin  # 被类继承 的登录装饰器
from django.views.generic import ListView  # 通用类视图

from item.models import Items


class ItemsListView(LoginRequiredMixin, ListView):
    """所有物品"""
    model = Items
    paginate_by = 10
    context_object_name = "items"
    template_name = "items/list.html"
