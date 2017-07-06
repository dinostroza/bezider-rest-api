#from rest_framework.serializers import ModelSerializer, SerializerMethodField, ListField
from rest_framework.serializers import *

from core.models import *
from social.models import *
from user.models import *

#-----------------------------------------------------------

class NewsCategorySerializer(ModelSerializer):
	class Meta:
		model = NewsCategory
		fields = [
			'name',
			'description',
			'tip',
			'date',
			'image'
		]

#-----------------------------------------------------------

class NewsTypeSerializer(ModelSerializer):
	class Meta:
		model = NewsType
		fields = [
			'name',
			'description',
			'tip',
			'category',
			'date',
			'image'
		]

#-----------------------------------------------------------


class UserNewsDetailSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')

class ReplyNewsDetailSerializer(ModelSerializer):
	user  = UserNewsDetailSerializer(read_only=True)
	class Meta:
		model = Reply
		fields = ('user', 'content', 'date')

class CommentNewsDetailSerializer(ModelSerializer):
	user  = UserNewsDetailSerializer(read_only=True)	
	replies = ReplyNewsDetailSerializer(many=True, read_only=True)
	class Meta:
		model = Comment
		fields = ('user', 'content','date', 'replies')

class ImagesNewsDetailSerializer(ModelSerializer):
	class Meta:
		model = NewsImage
		fields = ('user', 'image','date', 'location')

class NewsDetailSerializer(ModelSerializer):
	user      = UserNewsDetailSerializer(read_only=True)
	comments  = CommentNewsDetailSerializer(many=True, read_only=True)
	likers    = UserNewsDetailSerializer(many=True, read_only=True)
	followers = UserNewsDetailSerializer(many=True, read_only=True)
	witnesses = UserNewsDetailSerializer(many=True, read_only=True)
	images    = ImagesNewsDetailSerializer(many=True, read_only=True)
	class Meta:
		model = News
		fields = [
			'id',
			'user',
			'title',
			'type',
			'content',
			'latitude',
			'longitude',
			'date',
			'life',
			'num_visit',
			'num_share',
			'num_followers',
			'followers',
			'num_likes',
			'likers',
			'num_bookmarks',
			'bookmark_users',
			'num_witnesses',
			'witnesses',
			'num_comments',
			'comments',
			'num_images',
			'images'
		]

#-----------------------------------------------------------

class NewsCatcherSerializer(ModelSerializer):
	class Meta:
		model = NewsCatcher
		fields = [
			'user',
			'name',
			'description',
			'area',
			'location',
			'date'
		]