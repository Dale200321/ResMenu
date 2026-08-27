from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    is_featured = models.BooleanField(default=False, help_text='Show this item on the home page')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu:food_detail', args=[self.pk])


class SiteSettings(models.Model):
    """Singleton: restaurant-wide content the owner can edit from the admin."""

    restaurant_name = models.CharField(max_length=150, default='Restaurant Name')
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    intro_text = models.TextField(
        blank=True,
        default='Fresh ingredients, honest cooking, and a warm table waiting for you.',
        help_text='Short introduction shown on the home page.',
    )
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    opening_hours = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.restaurant_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class HomepageImage(models.Model):
    """One slide in the home page hero carousel. Add/reorder/remove from admin."""

    image = models.ImageField(upload_to='homepage/')
    caption = models.CharField(max_length=200, blank=True, help_text='Optional text shown over the image.')
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers show first.')

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.caption or f'Homepage image #{self.pk}'
