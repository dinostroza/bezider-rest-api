from rest_framework.filters import BaseFilterBackend
from django.contrib.gis.geos import Polygon
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.exceptions import ParseError

class NewsMapFilter(BaseFilterBackend):
	box_param = 'box'  # The URL query parameter which contains the box limits.

	def filter_queryset(self, request, queryset, view):
		box_string = request.query_params.get(self.box_param, None)
		#if there is not parameters given 
		if not box_string:
			raise ParseError('No coordinates supplied for parameter %s' %(self.box_param))

		#try to get left,top,right and bottom box coordinates
		try:
			l, t, r, b = (float(n) for n in box_string.split(','))
		#if fail, return an Parse Error
		except ValueError:
			raise ParseError('Invalid coordinates supplied for parameter %s' %(self.box_param))

		#if all ok, return news inside de box
		return queryset.in_box(l, t, r, b)