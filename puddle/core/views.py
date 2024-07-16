from django.shortcuts import render, redirect
from item.models import Category, Item

from .forms import SignUpForm

# Create your views here.
def index(request):
    items = Item.objects.filter(isSold = False)[0:6]
    """Item.objects.filter(isSold=False): Queries the Item model to get all items where the isSold field is False. 
    This returns a QuerySet of unsold items.
    
    [0:6]: Slices the QuerySet to get only the first 6 items. 
    This ensures that only the newest 6 unsold items are retrieved."""
    
    categories = Category.objects.all()   #  Queries the Category model to get all categories. This returns a QuerySet of all category objects
    # print(items)
    # for item in items:
    #     print(item.image)
    
    # for cat in categories:
    #     print(cat.items.count)
    return render(request, 'core/index.html',context={
        "categories": categories,
        "items": items
    })

def contact(request):
    return render(request, template_name= 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {
        'form': form
    })
