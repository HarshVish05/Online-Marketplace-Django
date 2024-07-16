from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item

# Create your views here.
@login_required
def dashboard(request):
    all_items = Item.objects.filter(created_by = request.user)

    return render(request= request, template_name= 'dashboard/dashboard.html', context={
        'items': all_items
    })




