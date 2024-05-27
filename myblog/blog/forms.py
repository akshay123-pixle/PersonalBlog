from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name...', 'data-sb-validations': 'required'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email...', 'data-sb-validations': 'required,email'}))
    phone = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number...', 'data-sb-validations': 'required'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message here...', 'style': 'height: 12rem', 'data-sb-validations': 'required'}))

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name...'}), label='Comment')


