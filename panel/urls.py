from django.urls import path, include
from .views import classesView, gradesView, unitView, studentView, scoreView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'classes', classesView, basename="classes")
router.register(r'grades', gradesView, basename="grades")
router.register(r'units', unitView, basename="units")
router.register(r'students', studentView, basename="students")
router.register(r'scores', scoreView, basename="scores")

urlpatterns = [
    # path('home/', home),
]

urlpatterns += router.urls