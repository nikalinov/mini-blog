from django import forms


class ProfileEditForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    bio = forms.CharField(max_length=500, widget=forms.Textarea)
    email = forms.EmailField(max_length=100)
    location = forms.CharField(max_length=100)

    contacts = {
        'website': forms.CharField(max_length=100, required=False),
        'github': forms.CharField(max_length=100, required=False),
        'twitter': forms.CharField(max_length=100, required=False),
        'instagram': forms.CharField(max_length=100, required=False),
        'facebook': forms.CharField(max_length=100, required=False),
    }
