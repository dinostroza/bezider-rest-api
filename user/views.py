from rest_framework.generics import *
from rest_framework.permissions import *
from user.models import *
from user.serializers import *

class PublicUserPerfilAPIView(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = PublicUserPerfilSerializer
	#permission_classes = [IsAuthenticated]