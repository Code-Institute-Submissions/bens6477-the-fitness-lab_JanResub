from django import forms
from .widgets import CustomClearableFileInput
from .models import Item, Category, Review


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields['category'].choices = display_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'


class ReviewForm(forms.ModelForm):
    """
    Form that allows users to add reviews to an item
    """
    class Meta:
        model = Review
        fields = ('body',)
