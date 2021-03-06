#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from zhaji.models import Note

class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text=u'请输入笔记的标题')
    content = forms.TextField(widget=forms.TextArea(), help_text=u'请输入笔记内容')

    class Meta:
        model = Note
        exclude = ('book', )

#class CategoryForm(forms.ModelForm):
#    name = forms.CharField(max_length=128, help_text=u"请输入类别名.")
#    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
#    class Meta:
        # Provide an association between the ModelForm and a model
#        model = Category
#        fields = ('name',)


#class PageForm(forms.ModelForm):
#    title = forms.CharField(max_length=128, help_text=u"请输入页面的标题.")
#    url = forms.URLField(max_length=200, help_text=u"请输入页面的地址.")
#    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

#    class Meta:
        # Provide an association between the ModelForm and a model
#        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
#        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

#    def clean(self):
#        cleaned_data = self.cleaned_data
#        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
#        if url and not url.startswith('http://'):
#            url = 'http://' + url
#            cleaned_data['url'] = url

#        return cleaned_data
