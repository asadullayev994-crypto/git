from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment, Like, Saved


def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})



def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    comments = product.comments.all()

    is_liked = False
    is_saved = False

    if request.user.is_authenticated:
        is_liked = Like.objects.filter(product=product, user=request.user).exists()
        is_saved = Saved.objects.filter(product=product, user=request.user).exists()

    context = {
        'product': product,
        'comments': comments,
        'is_liked': is_liked,
        'is_saved': is_saved,
    }

    return render(request, 'products/detail.html', context)



def like_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.user.is_authenticated:
        like, created = Like.objects.get_or_create(product=product, user=request.user)

        if not created:
            like.delete()

    return redirect('product_detail', id=id)



def save_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.user.is_authenticated:
        saved, created = Saved.objects.get_or_create(product=product, user=request.user)

        if not created:
            saved.delete()

    return redirect('product_detail', id=id)



def add_comment(request, id):
    product = get_object_or_404(Product, id=id)

    if request.user.is_authenticated and request.method == "POST":
        text = request.POST.get('text')

        if text:
            Comment.objects.create(
                product=product,
                user=request.user,
                text=text
            )

    return redirect('product_detail', id=id)