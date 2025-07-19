from django import forms
import datetime

from .models import Birthday


# Для использования формы с моделями меняем класс на forms.ModelForm.
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.

    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',})
        }


class BirthdayForm_draft(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(
        label='Фамилия', required=False, help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'date',},)
    )
 #   day = forms.DateField(label='Дата теста', initial=datetime.date.today)



class ContestForm(forms.Form):
    title = forms.CharField(
        label='Название',
        max_length=20
    )
    description = forms.JSONField(
        label='Описание',
        widget=forms.Textarea(
            attrs={
                'cols': '20',
                'rows': '5',
                'maxlength': '3',
                'style': 'margin-left: 200px;',
            },
        ),

    )
    price = forms.DecimalField(
        label='Цена',
        decimal_places=2,
        min_value=10,
        max_value=100,
        help_text='Рекомендованная розничная цена',
 #       initial='10'
        initial={'price': 8},
    )
    comment = forms.JSONField(
        label='Комментарий',
        required=False,
        widget=forms.Textarea(attrs={'cols': '20', 'rows': '5'}),
  #      default=[1, 2, 3],
    )
