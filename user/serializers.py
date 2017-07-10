from rest_framework.serializers import ModelSerializer, SerializerMethodField,PrimaryKeyRelatedField

from user.models import *
from core.models import *

class PublicUserPerfilNewsSerializer(ModelSerializer):
	class Meta:
		model = News
		fields = [
			'id',
			'title',
			'type',
			'content',
			'date',
			'life',
			'num_visit',
			'num_share',
			'num_followers',
			'num_likes',
			'num_witnesses',
			'num_comments',
			'num_images',
		]

class PublicUserPerfilSerializer(ModelSerializer):
	news = PublicUserPerfilNewsSerializer(many=True, read_only=True)
	class Meta:
		model = User
		fields = [
			'username',
			'profile_picture',
			'first_name',
			'date_joined',
			'last_name',
			'self_description',
			'points',
			'rank',
			'num_news',
			'news',
			'num_comments',
			'num_witnesses',
			'num_catchers',
			'num_followers'
		]