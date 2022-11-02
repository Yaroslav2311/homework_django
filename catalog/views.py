from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from .forms import PersonForm, Triangle
from .models import Person


def triangle(request):
    if 'submit' in request.GET:
        form = Triangle(request.GET)
        if form.is_valid():
            leg1 = int(form.cleaned_data['leg1'])
            leg2 = int(form.cleaned_data['leg2'])
            hypotenuse = ((leg1 ** 2) + (leg2 ** 2)) ** 0.5
            return render(request, 'catalog/triangle.html', {'form': form, 'hypotenuse': hypotenuse})
    else:
        form = Triangle()
        return render(request, 'catalog/triangle.html', {'form': form})


def person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:person')
    else:
        form = PersonForm()
    return render(request, 'catalog/person.html', {'form': form})


def update_person(request, pk):
    obj = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('catalog:person')

    else:
        form = PersonForm(instance=obj)
    return render(request, 'catalog/update_person.html', {'form': form, 'obj': obj})
