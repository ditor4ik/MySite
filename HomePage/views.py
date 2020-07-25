from django.shortcuts import render, get_object_or_404
from Content.models import BookModel
# Create your views here.
def index(request):
    Buff = BookModel.objects.all()
    return render(request,"HomePage/base.html", {'DataBook': Buff})
