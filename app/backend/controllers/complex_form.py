from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .common import get_base_page_information

@login_required
def index(request):
    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'Complex Form'),
    }
    return render(request, 'complex_form/index.html', context)
