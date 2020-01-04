from django.shortcuts import render


def base(request):
    context = {
        'base': base
    }
    return render(request, "base.html", context)
