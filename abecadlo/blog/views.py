from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # new
from django.urls import reverse_lazy  # new
from django.shortcuts import get_object_or_404, render, redirect
from .forms import Suma

from .models import Post
"""
def suma_old(request,pk):
    post = get_object_or_404(Post, pk=pk)
    tmp=post.liczby.split()
    for i in range(0, len(tmp)):
        tmp[i]=int(tmp[i])  
    post.suma=sum(tmp)
    post.save()
    return render(request, 'post_detail.html', {'post': post})
"""

def CIRconvert(request):
    print('views')
    if request.method == 'POST':
        form = Suma(request.POST)
        if form.is_valid():
            from urllib.request import urlopen
            from urllib.parse import quote
            print('if is valid')
            body = form.cleaned_data["pole_nazwa"]
            title ='SMILES'
            author = "test"
            url = 'http://cactus.nci.nih.gov/chemical/structure/' + body + '/smiles'
            print('url')
            ans = urlopen(url).read().decode('utf8')
            post = Post(nazwa=body, smiles=ans, author=author)
            post.save()
            print(post.id)
            return redirect('/')
    else:
        form = Suma()
    return render(request, 'suma.html', {'form': form })

"""
def suma(request):
      if request.method == 'POST':
          form = Suma(request.POST)
          if form.is_valid():
              body = form.cleaned_data["body"]
              title ='SMILES'
              author = "test"
              tmp=body.split()
              for i in range(0, len(tmp)):
                    tmp[i]=int(tmp[i])  
              suma=sum(tmp)
              post = Post(body=body, title=title, author=author,suma=suma)
                       
              post.save()
              return redirect('/')
      else:
          form = Suma()
      return render(request, 'suma.html', {'form': form })
"""

class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body", "liczby","suma"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body", "liczby"]


class BlogDeleteView(DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
