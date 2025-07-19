from django.shortcuts import get_object_or_404, render, redirect

from .forms import BirthdayForm, ContestForm
from .models import Birthday
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown


def birthday(request, pk=None):
    # Если в запросе указан pk (если получен запрос на редактирование объекта):
    if pk is not None:
        instance = get_object_or_404(Birthday, pk=pk)
    else:
        instance = None

    form = BirthdayForm(request.POST or None, instance=instance)
    # Создаём словарь контекста сразу после инициализации формы.
    context = {'form': form}
    # Если форма валидна...
    if form.is_valid():
        print('Сюда доходит?')
        form.save()
        print(form.instance.__dict__)
        # ...вызовем функцию подсчёта дней:
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )
        # Обновляем словарь контекста: добавляем в него новый элемент.
        context.update({'birthday_countdown': birthday_countdown})

 #   print(form.__dict__)
    default_data = {'description': '1',  'comment': ''}#'title': 'Your name', } #'description': '',  'comment': ''}
    default_data2 = {'description': '1',}
    f = ContestForm(default_data, auto_id=False)
    f = ContestForm(initial={'price': 8, 'title': 'Your name', }, auto_id=False) # default_data, 'comment': ''
  #  f = ContestForm(default_data, auto_id=False) # default_data,
  #  context = {
   #     'form': form,
     #   'form2': f,
  #      'form2': ContestForm(),
  #  }
  #  print(context)
    return render(request, 'birthday/birthday.html', context=context)


def birthday_list(request):
    # Получаем все объекты модели Birthday из БД.
    birthdays = Birthday.objects.all()
    # Передаём их в контекст шаблона.
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context)


def edit_birthday(request, pk):
    # Находим запрошенный объект для редактирования по первичному ключу
    # или возвращаем 404 ошибку, если такого объекта нет.
    instance = get_object_or_404(Birthday, pk=pk)
  #  print(instance.__dict__)
    # Связываем форму с найденным объектом: передаём его в аргумент instance.
    form = BirthdayForm(request.POST or None, instance=instance)
#    print(form.__dict__)
 #   print(f'Самое первое поле : {form.instance.birthday}') 
    # Всё остальное без изменений.
    context = {'form': form}
    # Сохраняем данные, полученные из формы, и отправляем ответ:
    if form.is_valid():
        print('сюда заходит?')
  #      print(form.__dict__) 
#        print(f'Поле до form.save(): {form.instance.birthday}')
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday']
        )
        context.update({'birthday_countdown': birthday_countdown})
  #      print(form.__dict__) 
 #       print(f'Поле после is_valid: {form.instance.birthday}')
    return render(request, 'birthday/birthday.html', context)


def delete_birthday(request, pk):
    # Получаем объект модели или выбрасываем 404 ошибку.
    instance = get_object_or_404(Birthday, pk=pk)
    # В форму передаём только объект модели;
    # передавать в форму параметры запроса не нужно.
    form = BirthdayForm(instance=instance)
    context = {'form': form}
    # Если был получен POST-запрос...
    if request.method == 'POST':
        # ...удаляем объект:
        instance.delete()
        # ...и переадресовываем пользователя на страницу со списком записей.
        return redirect('birthday:list')
    # Если был получен GET-запрос — отображаем форму.
    return render(request, 'birthday/birthday.html', context)


def test(request):
    print(request)
    print(request.GET)
    return render(request, 'birthday/test_pages.html')
