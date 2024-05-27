from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from .models import Post,Contact,Comment
from .forms import ContactForm,CommentForm
from django.core.mail import send_mail
def index(request):
    # p=Post.objects.all()
    p=Post.objects.order_by('-created_at')
    return render(request,'index.html',{'posts':p})
def about(request):
    return render(request,'about.html')
def post(request ,pk):
    p=Post.objects.get(id=pk)
    # print(f'id is {p}')
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=post)
    return render(request,'post.html',{'posts':p,'comments':comments})


def comment_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    print("post", post)
    
    if request.method == 'POST':
        text = request.POST.get('text')
        comments= Comment.objects.create(post=post, name=request.user.username, text=text)
        print(f'the comment is {comments}')
        return redirect('post', pk=post_id) # get request in post 


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            print(name,email,phone,message)
            user=Contact(name=name,email=email,phone=phone,message=message)
            user.save()
            subject=f"Regarding {message}"
            message=f'{message} {phone}'
            send_mail(subject,message,email,['randomstring890@gmail.com'],fail_silently=False)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('/contact/')
           

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


