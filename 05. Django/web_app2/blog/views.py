from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

# Create your views here.

# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html' # 템플릿 파일명 변경 / 디폴트는 post_list
    context_object_name = 'posts' # 컨텍스트 객체 이름 변경 / 디폴트는 object_list
    paginate_by = 2 # 페이지네이션, 페이지 당 문서 건 수

# DetailView
class PostDV(DetailView):
    model = Post