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

    def clean_binaryimage(self):
        image = self.cleaned_data.get('binaryimage')
        with open(configpath, 'rb') as f:
            data = tomllib.load(f)
            image_size = data.get('image_validation')['image_size']
            image_format = data.get('image_validation')['image_format']
            image_size_error = data.get('image_validation')['image_size_error']
            image_format_error = data.get('image_validation')[
                'image_format_error']
            image_empty_error = data.get('image_validation')[
                'image_empty_error']

            if not image:
                raise ValidationError(image_empty_error)
            else:
                extension = image.name.split(".")[-1]
            if extension not in image_format:
                raise ValidationError(image_format_error)
            if image:
                if image.size > image_size:
                    raise ValidationError(image_size_error)
                    return image_file

        if image:
            if image.size > 1 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image size should be less than 1MB.")
            return image

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['binaryimage'].error_messages['invalid_image'] = 'Please upload a JPG or PNG image.'
