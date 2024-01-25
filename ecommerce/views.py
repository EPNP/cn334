from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6410742354 Napatsineee Puangbubpa views!')

def item_view(request, item_id):   
    context_data = {"item_id": item_id   }
    
    return render(request, 'index.html',context= context_data)

def page_view(request, pagename):   
    template_name = f"{pagename}.html" 
    context_data = {"page_content": f"{pagename}"}
    return render(request, template_name, context=context_data)