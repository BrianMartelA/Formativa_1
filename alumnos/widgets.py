from django import forms

class PasswordToggleWidget(forms.PasswordInput):
    template_name = 'widgets/password_toggle.html'
    
    class Media:
        js = ('js/password_toggle.js',)

    def __init__(self, attrs=None):
        super().__init__(attrs)
        if 'class' not in self.attrs:
            self.attrs['class'] = 'form-control'
        else:
            self.attrs['class'] += ' form-control'