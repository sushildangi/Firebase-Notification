from django import forms

class NameForm(forms.Form):
    message_text = forms.CharField(label='message_text', max_length=100)
    message_label = forms.CharField(label='message_label', max_length=100)
    title = forms.CharField(label='title', max_length=100)
    notification_type = forms.CharField(label='notification_type', max_length=100)
    image = forms.CharField(label='image', max_length=100)
    message = forms.CharField(label='message', max_length=100)
    url_product = forms.CharField(label='url_product', max_length=100)
    unit_price = forms.CharField(label='unit_price', max_length=100)
