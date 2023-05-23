from config import MyConfigClass
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
        setting_config = MyConfigClass().validation_setting()

        if image:
            if image.size > 1 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image size should be less than 1MB.")
            return image

        if not image:
            raise ValidationError(setting_config.image_empty_error)
        else:
            if image:
                extension = image.name.split(".")[-1]
            if extension not in setting_config.image_format:
                raise ValidationError(setting_config.image_format_error)
            if image.size > setting_config.image_size:
                raise ValidationError(setting_config.image_size_error)
            return image

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['binaryimage'].error_messages['invalid_image'] = 'Please upload a JPG or PNG image.'
