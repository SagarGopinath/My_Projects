from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post , Comment , Category
from .forms import PostForm,EditForm,DateFilterForm,CommentForm
from django.urls import reverse_lazy
class Homeview(ListView):
    model = Post
    template_name  = 'blog.html'
    ordering = ['-id']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = DateFilterForm(self.request.GET)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if start_date and end_date:
                queryset = queryset.filter(post_date__range=[start_date, end_date])
            elif start_date:
                queryset = queryset.filter(post_date__gte=start_date)
            elif end_date:
                queryset = queryset.filter(post_date__lte=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DateFilterForm(self.request.GET)
        return context
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'category.html', {'cats': cats, 'category_posts':category_posts})


class Articleview(DetailView):
    model = Post
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        context['comments'] = self.object.comments.all()  
        context['comment_form'] = CommentForm()  
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = self.object
            comment.author = request.user  
            comment.save()
            return redirect('article', pk=self.object.pk)  
                
        context = self.get_context_data()
        context['comment_form'] = comment_form
        return self.render_to_response(context)



class Addpost(CreateView):
    model = Post
    form_class = PostForm    
    template_name = 'add.html'

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update.html'
    form_class = EditForm

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    