# from django import forms
# from .models import *

# class ResumeForm(forms.ModelForm):
#     class Meta:
#         model = Resume
#         fields = ['Cv']
        
#     def clean_Cv(self):
#         Cv = self.cleaned_data['Cv']
#         if not Cv.name.endswith('.pdf'):
#             raise forms.ValidationError('Only PDF files are allowed.')
#         return Cv