from django import forms

riverChoices = (
    ("1", "River One"),
    ("2", "River Two"),
    ("3", "River Three"),
    ("4", "River Four"),
    ("5", "River Five"),
    ("6", "River Six"),
    ("7", "Personalized River Trip"),
)

class ContactForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)
    number = forms.CharField(label="Contact Phone Number", max_length=10)
    email = forms.CharField(label="Contact Email", max_length=250)
    trip = forms.ChoiceField(choices = riverChoices)
    comment = forms.CharField(widget=forms.Textarea)
    