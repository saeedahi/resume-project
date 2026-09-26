from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from user_module.models import User
from home.models import Skill, Tools, Projects, TimeLineRoad, Article, SocialLinks
from home.forms import ContactUsModelForm
from django.contrib import messages


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['user'] = User.objects.filter(is_superuser=True).first()
        skills = Skill.objects.all()
        context['skills'] = skills

        tools = Tools.objects.all()
        context['tools'] = tools

        timelines = TimeLineRoad.objects.all().order_by('start_date')
        context['timelines'] = timelines

        articles = Article.objects.all().order_by('pk')
        context['articles'] = articles

        contact_us_form = ContactUsModelForm()
        context['contact_us_form'] = contact_us_form

        social_links = SocialLinks.objects.all()
        context['social_links'] = social_links

        projects = Projects.objects.all()
        if projects:
            context['projects'] = projects

        return context

    def post(self, request, *args, **kwargs):
        contact_us_form = ContactUsModelForm(request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد')

            return redirect('home_page')

        return self.render_to_response(
            self.get_context_data(contact_us_form=contact_us_form)
        )
