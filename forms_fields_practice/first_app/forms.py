from django import forms
import datetime

FAVORITE_COLORS_CHOICES = [
    ("blue", "Blue"),
    ("green", "Green"),
    ("black", "Black"),
]


class ExampleForm(forms.Form):
    name = forms.CharField()
    name2 = forms.CharField(widget=forms.Textarea)
    name3 = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        required=False,
        max_length=6,
    )
    first_name = forms.CharField(initial="jr.")
    email = forms.EmailField(label="your email address")
    agree = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={"type": "date"}))
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=["1997", "1998", "1999"])
    )
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color2 = forms.ChoiceField(
        widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES
    )
    favorite_colors3 = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors4 = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )


class ExampleForm2(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label="your email address")
    agree = forms.BooleanField(initial=True)
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={"type": "date"}))
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)