from django.shortcuts import render

# Create your views here.

def usertype_index(request):
    return render(request, 'usertypes/index.html')
    
def usertype_create(request):
    return render(request, 'usertypes/index.html')

def usertype_edit(request, id):
    return render(request, 'usertypes/index.html')

def usertype_update(request):
    return render(request, 'usertypes/index.html')

def usertype_show(request, id):
    return render(request, 'usertypes/index.html')

def usertype_delete(request, id):
    return render(request, 'usertypes/index.html')

def usertype_store(request):
    return render(request, 'usertypes/index.html')
