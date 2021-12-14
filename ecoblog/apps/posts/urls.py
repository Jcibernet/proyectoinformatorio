from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    
    path('listar/', views.ListarPosteos, name = 'listar_posteos'),
    path('<int:pk>', views.DetallePost, name="detalle_post"),
    path('ods/<int:pk>', views.PostSobreODS, name="detalle_posts_ods"),
    path('nuevo/', views.NuevoPost.as_view(), name="nuevo_post")

]