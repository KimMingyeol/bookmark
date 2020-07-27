from django.shortcuts import render

# Create your views here.
#이제부터 class형 view 짠다. 계속 변수명까지 미리 세팅된 generic view 이용
#class형 view에서는 장고가 미리 준비해둔 기능들을 class 상속받아 쓰는 형태이다.
from django.views.generic.list import ListView
from .models import Bookmark
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6
    #아마 ListView에서는 사용할 template 기본명이 '모델명_list' 인 듯

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url'] #CreateView에서 어떤 필드들을 입력받을 것인가
    success_url = reverse_lazy('list') #글쓰기 완료 후 이동할 페이지, 'list'는 urls.py에서 주소 확인 가능
    template_name_suffix = '_create'
    #CreateView에서는 template 기본명이 '모델명_form', 즉 여기선 'bookmark_form'인데 _ 뒤의 접미사를 create으로 바꾸어 'bookmark_create'으로 사용할 template명 변경

class BookmarkDetailView(DetailView):
    model = Bookmark #나머지 template_name이나 그런거는 알아서 자동 setting됨 generic의 힘..

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')