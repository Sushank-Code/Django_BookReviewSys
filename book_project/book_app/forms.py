from django import forms
from book_app.models import BookData

class BookForm(forms.ModelForm):
    class Meta:
        model = BookData
        fields = ["title","author","description","genre","isbn","publication_data"] 
        labels = {
            'title' : 'Title Name ',
            'author':'Author Name ',
            'description':'Description ',
            'genre':'Genre ',
            'isbn':'ISBN ',
            'publication_data':'Publication Date ',
        } 
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Book Title',
            }),
            'author':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Author Name',
            }),
            'description':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Write something about book..',
                'rows':4,
            }),
            'genre':forms.Select(attrs={
                'class':'form-control',
            }),
            'isbn':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter ISBN',
            }),
            'publication_data':forms.DateInput(
                attrs={
                'class':'form-control w-25',
                'type':'date',
                }
            ),
        }
        