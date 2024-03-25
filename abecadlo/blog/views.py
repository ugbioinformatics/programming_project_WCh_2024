from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # new
from django.urls import reverse_lazy  # new
from django.shortcuts import get_object_or_404, render, redirect
from .forms import Suma
import subprocess
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
def metoda(id):
    import fileinput
    from django.conf import settings
    
    with fileinput.FileInput(settings.MEDIA_ROOT+'/'+str(id)+"/molecule.mop", inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('PUT KEYWORDS HERE', 'AM1'), end='')
    return
    
def heat_energy(id):
    from django.conf import settings

    heat = ''
    energy = ''
    with open(settings.MEDIA_ROOT+'/'+str(id)+"/molecule.out", 'r') as file:
        nazwa = file.readlines()
    for line in nazwa:
        if line.startswith('          FINAL HEAT OF FORMATION ='):
            heat = line
        if line.startswith('          TOTAL ENERGY            ='):
            energy = line
    return heat, energy


def CIRconvert_Views(request):
    from django.conf import settings
    print('views')
    if request.method == 'POST':
        form = Suma(request.POST)
        if form.is_valid():
            from urllib.request import urlopen
            from urllib.parse import quote
            print('if is valid')
            body = form.cleaned_data["pole_nazwa"]
            if body != "":
                title ='SMILES'
                author = "test"
                url = 'http://cactus.nci.nih.gov/chemical/structure/' + body + '/smiles'
                print('url')
                ans = urlopen(url).read().decode('utf8')
                post = Post(nazwa=body, smiles=ans, author=author, cieplo=0, energia=0)
                post.save()
                print(post.id)
                from .Utilities import make_png_and_mop
                make_png_and_mop(ans, post.id)
                
            else:
                title ='SMILES'
                author = "test"
                post = Post(nazwa='jsd', smiles='pole_smiles', author=author, cieplo=0, energia=0)
                post.save()
                print(post.id)
                from .Utilities import make_png_and_mop
                make_png_and_mop(form.cleaned_data["pole_smiles"], post.id)
            metoda(post.id)
            subprocess.run(['/opt/mopac/MOPAC2016.exe', 'molecule.mop'], cwd = settings.MEDIA_ROOT+'/'+str(post.id))
            post.cieplo, post.energia = heat_energy(post.id)
            post.save()
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
