from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Coffee
from django.http import Http404
from django.shortcuts import render

def index(request):
    #Really dumb, just gets 5 entries, ordered by id...
    coffee_list = Coffee.objects.order_by('-id')[:5]
    #Get the template from log/templates/log/log_index.html
    template = loader.get_template('log/log_index.html')
    #Load the context with the model value.
    context = {'coffee_list': coffee_list}
    return HttpResponse(template.render(context, request))

    """
    Could also just do something like this, for shorthand:
    
    coffee_list = Coffee.objects.order_by('-id')[:5]
    context = {'coffee_list': coffee_list}
    return render(request, 'polls/index.html', context)
    """

def coffee_detail(request, coffee):
    try:
        #This is how you get an object.
        #You can also skip all the try, except stuff with "get_object_or_404()"
        coffee = coffee.objects.get(pk=question_id)
        response = "You're viewing the detail for coffee %s"
    except coffee.DoesNotExist:
        raise Http404("Coffee does not exist")
    return HttpResponse(response % coffee)

def roasts(request, coffee):
    return HttpResponse("Requesting roasts for Coffee %s." % coffee)