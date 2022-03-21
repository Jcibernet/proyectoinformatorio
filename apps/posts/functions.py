
from .models import Categoria

def obtenerCategorias():

    categorias = Categoria.objects.all()

    return categorias

