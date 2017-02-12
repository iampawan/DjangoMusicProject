from django.http import HttpResponse
from .models import Album
from django.template import loader

def index(request):

    html = ''
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')

    context ={
        'all_albums' : all_albums,
    }

    # for album in all_albums:
    #     url = "/music/"+str(album.id)+"/"
    #     html += "<a href ="+url+">"+album.album_title+"</a><br>"

    return HttpResponse(template.render(context,request))


def detail(request,album_id):
    return HttpResponse("<H1> Details of Album_id : "+str(album_id)+"</H1>")