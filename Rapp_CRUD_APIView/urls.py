from django.conf.urls import url
from . import views
app_name ='Rapp_CURD_APIView'
urlpatterns =[
    url(r'^m/(?P<pk>[0-9]+)$',views.M_View.as_view()),
    url(r'^m_l$',views.ML_View.as_view()),
    url(r'^a/(?P<pk>[0-9]+)$',views.A_View.as_view()),
    url(r'^a_l$',views.AL_View.as_view())
]

#  http --json POST http://127.0.0.1:8000/api-token-auth/username="vinod" password="vinod"


#  http --json POST http://127.0.0.1:8000/api/musicians/Authorization: "Token xza35
#                                       46u6tffrtyht98765hkrry3r4tgh32gryrg"


#  http --json POST http://127.0.0.1:8000/products/p_id="105"
#                          p_name="mobile" p_cost="10000.00" p_mfd="2018-2-5" p_exd="2025-5-5"


#  http --json POST http://127.0.0.1:8000/authapp/products/p_id="105"
#            p_name="mobile" p_cost="10000.00" p_mfd="2018-2-5" p_exd="2025-5-5" Authorization:
#            "Token xza3546u6tffrtyht98765hkrry3r4tgh32gryrg"

#  http --json DELETE http://127.0.0.1:8000/authapp/products/105/Authorization: "Token xza35
#                                       46u6tffrtyht98765hkrry3r4tgh32gryrg"