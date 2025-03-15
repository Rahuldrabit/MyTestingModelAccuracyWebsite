from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MachineLearning/',include('machine_learning.urls')),
    path('DeepLearning/',include('DeepLearning.urls')),
    path('DataAnalysis/',include('DataAnalysis.urls')),
    path('AboutUs/',include('AboutUs.urls')),
    path('Blog/',include('Blogs.urls')),
]
