from django.urls import path, include
from . import views


app_name = 'home'
bucket_urls = [
	path('', views.BucketHome.as_view(), name='bucket'),
	path('delet_obj_buckey/<key>', views.DeleteBucketObject.as_view(), name='delete_obj_bucket'),
]

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('category/<slug:category_slug>/', views.CategoryView.as_view(), name='category_filter'),
	path('bucket/', include(bucket_urls)),
	path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]