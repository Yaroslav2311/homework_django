from django.shortcuts import render

from .forms import Triagle


def foo(request):
    if 'submit' in request.GET:
        form = Triagle()
        leg1 = int(request.GET.get('leg1'))
        leg2 = int(request.GET.get('leg2'))
        hypotenuse = ((leg1 ** 2) + (leg2 ** 2)) ** 0.5
        return render(request, 'catalog/triangle.html', {'form': form, 'hypotenuse': hypotenuse})
    else:
        form = Triagle()
        return render(request, 'catalog/triangle.html', {'form': form})
