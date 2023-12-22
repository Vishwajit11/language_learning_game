from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
# from .views import GeneratePdf
app_name = "MyApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("language/", views.language, name="language"),
    path("test1e/", views.test1e, name="test1e"),
    path("test2e/", views.test2e, name="test2e"),
    path("test3e/", views.test3e, name="test3e"),
    path("languageh/", views.languageh, name="languageh"),
    path("test1h/", views.test1h, name="test1h"),
    path("test2h/", views.test2h, name="test2h"),
    path("test3h/", views.test3h, name="test3h"),



]