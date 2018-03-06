from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home(request):
    # template = loader.get_template('exam/dashboard/index.html')
    # context = {
    #     'sabin': 'sabin',
    # }
    # return HttpResponse(template.render(context, request))
    context = {'sabin': 'sabin'}
    return render(request, 'exam/dashboard/index.html', context)
