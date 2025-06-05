from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .common import get_base_page_information


def my_profile(request):

    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'My Account'),
    }
    return render(request, 'account/profile.html', context)

'''
def view_account(request):

    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'View Account'),
    }
    return render(request, 'account/index.html', context)

def create(request):

    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'Create Account'),
    }
    return render(request, 'account/create/index.html', context)

def sign_in(request):

    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'Sign in'),
    }
    return render(request, 'account/sign_in/index.html', context)

def forgot_password(request):

    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'Forgot Password'),
    }
    return render(request, 'account/forgot_password/index.html', context)

@login_required
def change_password(request):

    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'Change Password'),
    }
    return render(request, 'account/change_password/index.html', context)
'''
