from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from product.models import Product, Category
from order.models import Order, OrderProduct
from home.models import FAQ, ContactMessage
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
# Create your views here.
############### BASE METHOD ###############
def view_403(request):
    return render(request,'403.html')

@login_required
def view_admin(request):
    if not request.user.is_superuser:
        return redirect('403')
    return render(request,'manage.html')

############### PRODUCT ###############
@login_required
def view_product(request):
    if not request.user.is_superuser:
        return redirect('403')
    all_product = Product.objects.all()
    context = {
        'all_product': all_product
    }
    return render(request,'product/index.html',context)

@login_required(login_url='login')
def delete_product(request, id):
    if not request.user.is_superuser:
        return redirect('403')

    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return redirect(request.META.get('HTTP_REFERER', 'view_product'))

    product.delete()

    return redirect('view_product')

@login_required(login_url='login')
def view_create_product(request):
    if not request.user.is_superuser:
        return redirect('403')
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        keywords = request.POST.get('keywords')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        amount = request.POST.get('amount')
        minamount = request.POST.get('minamount')
        variant = request.POST.get('variant')
        detail = request.POST.get('detail')
        slug = request.POST.get('slug')
        status = request.POST.get('status')
        product = Product(
            title=title,
            category_id=category_id,
            keywords=keywords,
            description=description,
            image=image,
            price=price,
            amount=amount,
            minamount=minamount,
            variant=variant,
            detail=detail,
            slug=slug,
            status=status
        )
        product.save()
        return redirect('view_product')
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request,'product/create.html', context)

@login_required(login_url='login')
def view_edit_product(request, id):
    if not request.user.is_superuser:
        return redirect('403')
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return redirect(request.META.get('HTTP_REFERER', 'view_product'))
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        new_title = request.POST.get('title')
        new_category_id = request.POST.get('category')
        new_keywords = request.POST.get('keywords')
        new_description = request.POST.get('description')
        new_image = request.FILES.get('image')
        new_price = request.POST.get('price')
        new_amount = request.POST.get('amount')
        new_minamount = request.POST.get('minamount')
        new_variant = request.POST.get('variant')
        new_detail = request.POST.get('detail')
        new_slug = request.POST.get('slug')
        new_status = request.POST.get('status')
        #update
        product.title = new_title
        product.category_id = new_category_id
        product.keywords = new_keywords
        product.description = new_description
        #image
        if new_image:
            product.image = new_image
        product.price = new_price
        product.amount = new_amount
        product.minamount = new_minamount
        product.variant = new_variant
        product.detail = new_detail
        product.slug = new_slug
        product.status = new_status
        product.save()
        return redirect('view_product')
    #context
    categories = Category.objects.all()
    variant_list = ['Size', 'Color', 'Size-Color']
    context = {
        'product': product,
        'categories': categories,
        'variant_list': variant_list,
    }
    return render(request,'product/edit.html', context)

############### CATEGORY ###############
@login_required
def view_category(request):
    if not request.user.is_superuser:
        return redirect('403')
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request,'category/index.html',context)


@login_required(login_url='login')
def delete_category(request, id):
    if not request.user.is_superuser:
        return redirect('403')

    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return redirect(request.META.get('HTTP_REFERER', 'view_category'))

    category.delete()

    return redirect('view_category')

@login_required(login_url='login')
def view_edit_category(request, id):
    if not request.user.is_superuser:
        return redirect('403')
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return redirect(request.META.get('HTTP_REFERER', 'view_category'))
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        new_title = request.POST.get('title')
        new_keywords = request.POST.get('keywords')
        new_description = request.POST.get('description')
        new_image = request.FILES.get('image')
        new_slug = request.POST.get('slug')
        new_status = request.POST.get('status')
        #update
        category.title = new_title
        category.keywords = new_keywords
        category.description = new_description
        #image
        if new_image:
            category.image = new_image
        category.slug = new_slug
        category.status = new_status
        category.save()
        return redirect('view_category')
    return render(request, 'category/edit.html',context={'category': category})

@login_required(login_url='login')
def view_create_category(request):
    if not request.user.is_superuser:
        return redirect('403')
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        title = request.POST.get('title')
        keywords = request.POST.get('keywords')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        slug = request.POST.get('slug')
        status = request.POST.get('status')
        #create
        category = Category(title=title, keywords=keywords, description=description, image=image, slug=slug, status=status)
        category.save()
        return redirect('view_category')
    return render(request, 'category/create.html')

############### USER ###############    
@login_required
def view_user(request):
    if not request.user.is_superuser:
        return redirect('403')
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request,'user/index.html',context)

@login_required
def delete_user(request, id):
    if not request.user.is_superuser:
        return redirect('403')
    user = get_object_or_404(User, id=id)
    if user != request.user:
        user.delete()
        return redirect('view_user')
    return render(request,'user/index.html')

@login_required
def view_edit_user(request, id):
    if not request.user.is_superuser:
        return redirect('403')
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_password = request.POST.get('password')
        #update
        user.username = new_username
        user.email = new_email
        user.set_password(new_password)
        user.save()
        return redirect('view_user')
    return render(request,'user/edit.html', context={'user': user})


############### ORDER ###############    
@login_required
def view_order(request):
    if not request.user.is_superuser:
        return redirect('403')
    STATUS = (
        ('Mới', 'Mới'),
        ('Chấp nhận', 'Chấp nhận'),
        ('Đang chuẩn bị', 'Đang chuẩn bị'),
        ('Đang Ship', 'Đang Ship'),
        ('Hoàn Thành', 'Hoàn Thành'),
        ('Đã hủy', 'Đã hủy'),
    )
    orders = Order.objects.all()
    return render(request,'order/index.html', context={'orders': orders, 'STATUS': STATUS})

@login_required
def update_status_order(request,id_order):
    if not request.user.is_superuser:
        return redirect('403')
    order = get_object_or_404(Order, id=id_order)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('view_order')
    

@login_required
def view_order_detail(request,id_order):
    if not request.user.is_superuser:
        return redirect('403')
    order = get_object_or_404(Order, id=id_order)
    order_products = OrderProduct.objects.filter(order=order)
    return render(request,'order/detail.html',context={'order': order,'order_products': order_products})


############### FAQS ###############  
@login_required
def view_faq(request):
    if not request.user.is_superuser:
        return redirect('403')
    faqs = FAQ.objects.all()
    return render(request,'faq/index.html',context={'faqs': faqs})

@login_required
def view_create_faq(request):
    if not request.user.is_superuser:
        return redirect('403')
    if request.method == "POST":
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        ordernumber = request.POST.get('ordernumber')
        status = request.POST.get('status')
        faq = FAQ(ordernumber=ordernumber,question=question, answer=answer, status=status)
        faq.save()
        return redirect('view_faq')
    return render(request, 'faq/create.html')

@login_required
def delete_faq(request, faq_id):
    if not request.user.is_superuser:
        return redirect('403')
    faq = get_object_or_404(FAQ, id=faq_id)
    if faq:
        faq.delete()
        return redirect('view_faq')

@login_required
def view_edit_faq(request, faq_id):
    if not request.user.is_superuser:
        return redirect('403')
    faq = get_object_or_404(FAQ, id=faq_id)
    if request.method == "POST":
        new_question = request.POST.get('question')
        new_answer = request.POST.get('answer')
        new_ordernumber = request.POST.get('ordernumber')
        new_status = request.POST.get('status')
        #update
        faq.question = new_question
        faq.answer = new_answer
        faq.ordernumber = new_ordernumber
        faq.status = new_status
        faq.save()
        return redirect('view_faq')
    return render(request,'faq/edit.html',context={'faq': faq})
############### CONTACT ###############  
@login_required
def view_contact(request):
    if not request.user.is_superuser:
        return redirect('403')
    contacts = ContactMessage.objects.all()
    return render(request,'contact/index.html',context={'contacts': contacts})

@login_required
def delete_contact(request,contact_id):
    if not request.user.is_superuser:
        return redirect('403')
    try:
        contact = get_object_or_404(ContactMessage,id=contact_id)
    except ContactMessage.DoesNotExist:
        return redirect(request.META.get('HTTP_REFERER', 'view_contact'))
    contact.delete()
    return redirect('view_contact')