from django.shortcuts import render

from .forms import Triangle


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
