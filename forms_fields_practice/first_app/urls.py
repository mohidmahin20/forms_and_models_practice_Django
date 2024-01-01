from django.urls import path
from first_app.views import one, two

urlpatterns = [path("", one, name="one"), path("two/", two, name="two")]