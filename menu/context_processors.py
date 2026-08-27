from .models import SiteSettings


def restaurant_info(request):
    site = SiteSettings.load()
    return {
        'site': site,
        'RESTAURANT_NAME': site.restaurant_name,
        'RESTAURANT_ADDRESS': site.address,
        'RESTAURANT_PHONE': site.phone,
        'RESTAURANT_EMAIL': site.email,
        'RESTAURANT_HOURS': site.opening_hours,
    }
