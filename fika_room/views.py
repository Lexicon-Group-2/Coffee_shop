from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import ChatPost
from django.urls import reverse


def fika_room(request):
  messages = ChatPost.objects.all()
  images = []
  for msg in messages.iterator():
    try:
      images.append(msg.user.profile.image.url)
    except:
      images.append('/media/profile_pics/default.png')
  
  if request.method == 'POST':
    username = request.user
    content  = request.POST.get('message')
    if len(content) > 0:
      message = ChatPost(user=username, content=content)
      message.save()
    return HttpResponseRedirect('/fika_room')
    
  context = {
    'msgs' : messages,
    'count': len(messages),
    'images':images,
  }
  
  for i, img in enumerate(images):
    print(i, img)
  return render(request, 'fika_room/fika_room.html', context)

def article_1(request):
  return render(request, 'fika_room/article_1.html', {})
  
def article_2(request):
  return render(request, 'fika_room/article_2.html', {})
  
def article_3(request):
  return render(request, 'fika_room/article_3.html', {})