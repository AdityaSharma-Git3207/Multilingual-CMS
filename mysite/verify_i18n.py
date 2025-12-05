import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.dev")
django.setup()

from wagtail.models import Locale, Page
from home.models import HomePage

def verify():
    print("Verifying Locales...")
    # Check Locales
    en_locale, created = Locale.objects.get_or_create(language_code='en')
    fr_locale, created = Locale.objects.get_or_create(language_code='fr')
    
    print(f"English Locale: {en_locale}")
    print(f"French Locale: {fr_locale}")

    # Check Homepage
    print("\nVerifying Homepage...")
    homepage = HomePage.objects.first()
    if not homepage:
        print("No Homepage found. Creating one...")
        root = Page.objects.get(id=1) # Usually root is 1 or 2
        homepage = HomePage(title="Home", body="<p>Welcome to the English site.</p>")
        root.add_child(instance=homepage)
        homepage.save_revision().publish()
    else:
        print(f"Homepage found: {homepage.title}")
        if not homepage.body:
             homepage.body = "<p>Welcome to the English site.</p>"
             homepage.save_revision().publish()

    # Check Translation
    print("\nVerifying Translation...")
    fr_homepage = homepage.get_translation_or_none(fr_locale)
    if not fr_homepage:
        print("Creating French translation...")
        fr_homepage = homepage.copy_for_translation(fr_locale)
        fr_homepage.title = "Accueil"
        fr_homepage.body = "<p>Bienvenue sur le site français.</p>"
        fr_homepage.save_revision().publish()
        print("French translation created.")
    else:
        print(f"French translation found: {fr_homepage.title}")

    print("\nVerification Complete.")

if __name__ == "__main__":
    verify()
