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

def CIRconvert(ids):
    if request.method == 'POST':
          form = CIRconvert(request.POST)
        if form.is_valid():
            body = form.cleaned_data["body"]
            title ='SMILES'
            author = "test"
            tmp=body.split()
            try:
                url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles' 
                ans = urlopen(url).read().decode('utf8')
                return ans
            except:
                return 'Did not work'
            post = Post(body=body, title=title, author=author,suma=suma)
            post.save()
            return redirect('/')
        identifiers = input()
        print(CIRconvert(identifiers))
    else:
          form = CIRconvert()
      return render(request, 'CIRconvert.html', {'form': form })


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