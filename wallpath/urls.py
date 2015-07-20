from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',

    url(r'^$', views.home, name="home"),
    url(r'^patient_detail/(?P<pk>.*)/$', views.patient_detail, name='patient_detail'),
    url(r'^add_patient/$', views.add_patient, name='add_patient'),
    url(r'^Email/$', views.Email, name='Email'), #This is going to be the link that sends the email
    url(r'^emailsetup/$', views.emailsetup, name='emailsetup'), #This is the setup page for the email
    url(r'^admin/', include(admin.site.urls)),
    url(r'^survey/$', views.survey_detail), #api call
    url(r'^user/(?P<pk>.*)/$', views.user_check),#api call

    (r'^accounts/',
                        include('registration.backends.simple.urls')),
                       # Password URL workarounds for Django 1.6:
                       #   http://stackoverflow.com/questions/19985103/

                       url(r'^password/change/$', auth_views.password_change,
                           name='password_change'),
                       url(r'^password/change/done/$',
                           auth_views.password_change_done,
                           name='password_change_done'),
                       url(r'^password/reset/$', auth_views.password_reset,
                           name='password_reset'),
                       url(r'^accounts/password/reset/done/$',
                           auth_views.password_reset_done,
                           name='password_reset_done'),
                       url(r'^password/reset/complete/$',
                           auth_views.password_reset_complete,
                           name='password_reset_complete'),
                       # (Line too long) pylint: disable=C0301
                       url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                           auth_views.password_reset_confirm,
                           name='password_reset_confirm'),

)

