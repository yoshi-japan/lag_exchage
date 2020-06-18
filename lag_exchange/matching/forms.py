from django.forms import ModelForm
from . models import Post

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields=[
            'user_name',
            'country',
            # should be remotehour_url
            'zoom_url',

        ]