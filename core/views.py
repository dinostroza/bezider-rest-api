from django.db.models import Q
from django.contrib.gis.geos import Polygon
#from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.generics import *
#from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import *
from core.models import *
from social.models import *
from core.serializers import *
from social.serializers import *

class NewsDetailAPIView(RetrieveAPIView):
	queryset = News.objects.all()
	serializer_class = NewsDetailSerializer
	#permission_classes = [IsAuthenticated]

class NewsTypeAPIView(RetrieveAPIView):
	queryset = NewsType.objects.all()
	serializer_class = NewsTypeSerializer
	#permission_classes = [IsAuthenticated]

class NewsCategoryAPIView(RetrieveAPIView):
	queryset = NewsCategory.objects.all()
	serializer_class = NewsCategorySerializer
	#permission_classes = [IsAuthenticated]

class NewsCatcherAPIView(RetrieveAPIView):
	queryset = NewsCatcher.objects.all()
	serializer_class = NewsCatcherSerializer
	#permission_classes = [IsAuthenticated]