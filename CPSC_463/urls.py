"""CPSC_463 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from patient import views as patient_views
from dashboard import views as dash_views
from doctors import views as doc_views


# Added to block unauthenticated users from accessing anything other than
# login and sign up pages ====> login_required(whatever view)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.login, name='login'),
    path('signup/', patient_views.patient_signup, name='signup'),
    path('signup/personal_information/', patient_views.personal_info_signup, name='personal_info_signup'),
    path('signup/medical_information/', patient_views.medical_info_signup, name='medical_info_signup'),
    path('home/', login_required(dash_views.home), name='home'),
    path('logout/', login_required(auth_views.logout), {'next_page': '/'}, name='logout'),
    path('schedule/', login_required(dash_views.schedule_appt), name='schedule_appt'),
    path('inbox/', login_required(dash_views.inbox), name='inbox'),
    path('provider/', login_required(dash_views.provider), name='provider'),
    path('recipes/', login_required(dash_views.recipes), name='recipes'),
    path('lgout/', login_required(dash_views.before_logout), name='b4-logout'),
    path('profile/', login_required(patient_views.view_profile), name='view_profile'),
    path('edit_profile/', login_required(patient_views.edit_profile), name='edit_profile'),
    path('doctors/', login_required(doc_views.doctors), name='doctors'),
    path('ajax_search/', doc_views.ajax_search),
    path('ajax_inbox_history/', dash_views.ajax_inbox_history),
    path('ajax_inbox/', dash_views.ajax_inbox),
]
