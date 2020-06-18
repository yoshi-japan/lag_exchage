from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, FormView, CreateView
from django.urls import reverse_lazy

from . models import Post
from . forms import PostCreateForm

# Create your views here.

class PostListView(ListView):

    template_name = 'matching/home.html'
    queryset = Post.objects.order_by('-created')
    context_object_name = 'post_list'
    paginate_by = 8
    page_kwarg = 'p'


class PostCreateView(CreateView):
    template_name = 'matching/create_post.html'
    form_class = PostCreateForm
    model = Post
    success_url = reverse_lazy("matching:home")

    def form_valid(self, form):
        context = {'form':form}
        if self.request.POST.get('next', "") == 'confirm':
            return render(self.request, 'matching/confirm_post.html', context)
        if self.request.POST.get('next', '') == 'back':
            return render(self.request, 'matching/create_post.html', context)
        if self.request.POST.get('next', "") == 'create':
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy('matching:home'))



def post_create(request):
    template_name = 'matching/create_post.html'
    context = {}
    if request.method == "GET":
        context['form'] = PostCreateForm()
        return render(request, template_name, context)

    if request.method == 'POST':
        post_form = PostCreateForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect(reverse_lazy("matching:home"))
        else:
            context['form'] = post_form
            return render(request, template_name, context)
