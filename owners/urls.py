from django.urls import path
from owners.views import CatAndOpenerView, OpenerView, CatView

urlpatterns = [
    path('openers', OpenerView.as_view()),
    path('cats', CatView.as_view()),
    path('catsandopeners', CatAndOpenerView.as_view()),
]