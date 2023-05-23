from config.validation import Validationfiles
from config.config import Configfiles
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # call the validation_setting function
        self.config = Validationfiles().validation_setting()

    def clean_binaryimage(self):
        image = self.cleaned_data.get('binaryimage')

        if not image:
            raise ValidationError(self.config.image_empty_error)
        else:
            if image:
                extension = image.name.split(".")[-1]
            if extension not in self.config.image_format:
                raise ValidationError(self.config.image_format_error)
            if image.size > self.config.image_size:
                raise ValidationError(self.config.image_size_error)
            return image
