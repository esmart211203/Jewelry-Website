from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
    path('view/', views.view_admin,name='view_admin'),
    path('403', views.view_403,name='403'),
    ### product ###
    path('view-product', views.view_product, name='view_product'),
    path('create-product/', views.view_create_product, name='create_product'),
    path('delete-product/<int:id>', views.delete_product, name='delete_product'),
    path('edit-product/<int:id>', views.view_edit_product, name='edit_product'),
    ### category ###
    path('view-category', views.view_category, name='view_category'),
    path('create-category/', views.view_create_category, name='create_category'),
    path('delete-category/<int:id>', views.delete_category, name='delete_category'),
    path('edit-category/<int:id>', views.view_edit_category, name='edit_category'),
    ### user ###
    path('view-user', views.view_user, name='view_user'),
    path('delete-user/<int:id>', views.delete_user, name='delete_user'),
    path('edit-user/<int:id>', views.view_edit_user, name='edit_user'),
    ### order ###
    path('view-order', views.view_order, name='view_order'),
    path('update-status-order/<int:id_order>', views.update_status_order, name='update_order'),
    path('order-detail/<int:id_order>', views.view_order_detail, name='order_detail'),
    ### faqs ###
    path('view-faq', views.view_faq, name='view_faq'),
    path('view-create-faq', views.view_create_faq, name='create_faq'),
    path('edit-faq/<int:faq_id>', views.view_edit_faq, name='edit_faq'),
    path('delete-faq/<int:faq_id>', views.delete_faq, name='delete_faq'),
    ### contact ###
    path('view-contact', views.view_contact, name='view_contact'),
    path('delete-contact/<int:contact_id>', views.delete_contact, name='delete_contact'),
]
