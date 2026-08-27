from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Category, HomepageImage, MenuItem, SiteSettings


def home(request):
    featured_items = MenuItem.objects.filter(is_featured=True)[:6]
    homepage_images = HomepageImage.objects.all()
    context = {
        'featured_items': featured_items,
        'homepage_images': homepage_images,
    }
    return render(request, 'menu/home.html', context)


def menu_list(request):
    items = MenuItem.objects.select_related('category').all()
    categories = Category.objects.all()

    selected_category = request.GET.get('category')
    if selected_category:
        items = items.filter(category__slug=selected_category)

    context = {
        'items': items,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'menu/menu_list.html', context)


def food_detail(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    return render(request, 'menu/food_detail.html', {'item': item})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            site = SiteSettings.load()
            send_mail(
                subject=f"[Contact Form] {data['subject']}",
                message=f"From: {data['name']} <{data['email']}>\n\n{data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[site.email or settings.DEFAULT_FROM_EMAIL],
            )
            messages.success(request, 'Thanks for reaching out! We will get back to you soon.')
            return redirect('menu:contact')
    else:
        form = ContactForm()

    return render(request, 'menu/contact.html', {'form': form})
