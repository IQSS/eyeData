from django import forms
from eyedata.models import DataSet

class DataSetRequestForm(forms.ModelForm):
  name = forms.CharField(max_length=128, help_text="Please Enter DataSet Name")
  views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

  # An inline class to provide additional information on the form.
  class Meta:
    # Provide an association between the ModelForm and a model
    model = Category

    fields = ('name')
