from django import forms
from videos.models import Video

class VideoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
                {'placeholder': 'Enter Title', 'class': 'textinput textInput form-control'})
        self.fields['author'].widget.attrs.update(
                {'placeholder': 'Enter Author', 'class': 'textinput textInput form-control'})
        self.fields['description'].widget.attrs.update(
                {'placeholder': 'Enter Description', 'class': 'contact_form_phone input_field'})
        self.fields['youtube_vid'].widget.attrs.update({
                'placeholder': 'Your youtube ID', 'class': 'text_field contact_form_message'})
        self.fields['stars_count'].widget.attrs.update(
            {'placeholder': 'Your rating', 'class': 'text_field contact_form_message'})

    def setData(self, data):
        self.data = data
        self.is_bound = True

    class Meta:
        model = Video
        fields = ['title', 'author', 'description', 'youtube_vid', 'stars_count', 'category_id', 'skill_level_id', 'is_active']

