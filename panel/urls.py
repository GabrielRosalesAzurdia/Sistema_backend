from django.urls import path, include
from .views import classesView, gradesView, unitView, studentView, scoreView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'classes', classesView, basename="classes")
# classes_list= classesView.as_view({
#     "get":"list",
#     "post":"create"
# })
router.register(r'grades', gradesView, basename="grades")
router.register(r'units', unitView, basename="units")
router.register(r'students', studentView, basename="students")
router.register(r'scores', scoreView, basename="scores")

urlpatterns = [
    #path("classes/", classes_list)
]

urlpatterns += router.urls