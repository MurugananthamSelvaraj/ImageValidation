from django import forms
from .models import Images
import tempfile
from django.core.exceptions import ValidationError
import tomllib
configpath = 'config.toml'


class ImageForm(forms.ModelForm):
    binaryimage = forms.ImageField(label='Image File')

    class Meta:
        model = Images
        fields = ('title', 'description', 'binaryimage')

        def clean_image(self):
            binaryimage = self.cleaned_data.get('binaryimage')
            temp_image = tempfile.NamedTemporaryFile(delete=True)
            temp_image.write(binaryimage.read())
            temp_image.flush()
            self.cleaned_data['binaryimage'] = temp_image.name
            return binaryimage
