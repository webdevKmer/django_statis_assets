from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


    def send_email(self):
        print(f"Sending Email from {self.cleaned_data['email']} with message : {self.cleaned_data['message']}")
