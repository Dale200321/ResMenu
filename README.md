# Restaurant Menu Website (Django)

A simple, responsive restaurant menu website. Customers can browse the menu,
filter by category, view food details, and send a message via the contact
form. The restaurant owner manages everything through the Django admin.

## Tech Stack

Python, Django, Django ORM, Django Admin, Django Templates, Bootstrap 5
(via CDN), SQLite.

## Setup Instructions

1. Activate the existing virtual environment:

   ```
   venv\Scripts\activate
   ```

2. Install dependencies (already installed in `venv`, run only if setting up fresh):

   ```
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```
   python manage.py migrate
   ```

4. Create an admin account:

   ```
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```
   python manage.py runserver
   ```

6. Visit the site:
   - Website: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Managing Menu Content

Log in to the admin panel and:

- Add **Categories** first (e.g. Starters, Mains, Desserts, Drinks).
- Add **Menu Items** with name, description, price, image, and category.
  Check "is_featured" to show an item on the home page.

Uploaded images are stored in `media/menu_items/`.

## Restaurant Details

The address, phone, email, and opening hours shown on the site are set in
`resmenu/settings.py` (`RESTAURANT_NAME`, `RESTAURANT_ADDRESS`,
`RESTAURANT_PHONE`, `RESTAURANT_EMAIL`, `RESTAURANT_HOURS`). Update these to
match the real restaurant.

## Contact Form

Submissions are sent via Django's email system to `RESTAURANT_EMAIL`. In
development, `EMAIL_BACKEND` is set to the console backend, so messages are
printed to the terminal running `runserver` instead of actually being
emailed. For production, replace it with an SMTP backend (e.g. Gmail,
SendGrid) in `resmenu/settings.py`.

## Project Structure

```
resmenu/        Project settings, root URLs
menu/           App: models, views, forms, admin, URLs
templates/      HTML templates (base + menu app pages)
static/css/     Custom stylesheet
media/          Uploaded menu item images (created at runtime)
```

## Notes for Production

Before deploying, be sure to:

- Set `DEBUG = False` and populate `ALLOWED_HOSTS`.
- Move `SECRET_KEY` and email credentials to environment variables.
- Configure a real SMTP `EMAIL_BACKEND`.
- Serve static/media files via a proper web server (not Django's dev server).
