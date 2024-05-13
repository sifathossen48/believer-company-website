
from django.forms import ModelForm

from Get_Quote_Page.models import GetQuote


class GetQuoteForm(ModelForm):
    class Meta:
        model = GetQuote
        fields = ['company', 'address', 'email', 'phone', 'message', ]
      