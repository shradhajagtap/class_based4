from django import forms

from .models import Contact

GENDER_CHOICES = [("male", "male"), ("female", "female")]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(),
            "phone_no": forms.NumberInput(),
            "mode_of_contact": forms.Select(attrs={"class": "form-control"}),
            "gender": forms.RadioSelect(choices=GENDER_CHOICES),
            "message": forms.Textarea({"rows": 5, "col": 5})
        }
