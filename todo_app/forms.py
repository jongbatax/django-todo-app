from django.forms import ModelForm, TextInput

from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["name"]
        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Enter todo e.g. Reading a Book",
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = ""
