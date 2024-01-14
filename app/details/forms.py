from django import forms


class SearchForm(forms.Form):
    mask = forms.CharField(max_length=13,required=False)


class DrawForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols':75, 'rows':38}), label='', required=False)
