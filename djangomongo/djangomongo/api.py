from rest_framework import routers
from escola import api_views as escola_views

router = routers.DefaultRouter()
router.register(r'professor', escola_views.ProfessorViewset)
router.register(r'curso', escola_views.CursoViewset)
router.register(r'aluno', escola_views.AlunoViewset)
router.register(r'user', escola_views.UserViewset)