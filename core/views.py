from rest_framework.generics import *
#from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import *
from core.models import *
from social.models import *
from core.serializers import *
from .filters import *


class NewsMapAPIView(ListAPIView):
	queryset = News.objects.all()
	serializer_class = NewsMapSerializer
	filter_backends = (NewsMapFilter,)
	#permission_classes = [IsAuthenticated]

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