from django.urls import path
from demo1 import views

urlpatterns = [
		path('form/',views.form, name='form'),
		path('adddata/',views.adddata, name='adddata'),
		path('getdata/',views.getdata),
		path('delete/<int:id>',views.delete),
		path('getdataforedit/<int:id>',views.getdataforedit),
		path('update/<int:id>',views.update)

		]