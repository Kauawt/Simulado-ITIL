from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = "homepage.html"


class LoginView(TemplateView):
    template_name = "loginpage.html"
