from django.contrib import admin
from django.urls import path, include
from backend.controllers import about, errors, home, account, complex_form
#from allauth.account.views import LoginView, SignupView

handler400 = errors.error_400
handler403 = errors.error_403
handler404 = errors.error_404
handler500 = errors.error_500

urlpatterns = [
    path('', home.index, name='home'),
    #path('account/', account.view_account, name='account_view'),
    #path('account/sign_in/', account.sign_in, name='account_sign_in'),
    #path('account/create/', account.create, name='account_create'),
    #path('account/forgot_password/', account.forgot_password, name='account_forgot_password'),
    #path('account/change_password/', account.change_password, name='account_change_password'),
    path('accounts/profile/', account.my_profile, name='account_profile'),
    path('about/', about.index, name='about'),
    path('complex_form/', complex_form.index, name='complex_form'),

    #path('allauth/layouts/base.html', accounts.view_account, name='account_view'),
    #path('account/sign_in/', LoginView.as_view(), name="account_sign_in" ),
    #path('account/create/', SignupView.as_view(), name="account_create" ),

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

]
