from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView
from Get_Quote_Page import forms

# Create your views here.
def quote(request):
    if request.method == 'POST':
        form = forms.GetQuoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully') # Redirect to a success page
        else:
            # Print form errors to console for debugging
            print(form.errors)
            messages.error(request, 'Invalid! Please try again.')
    else:
        form = forms.GetQuoteForm()
    context = {
        'form': form
    }
    return render(request, 'get-quote.html', context)
