from django.conf import settings
from rest_framework import generics

from ..models import User
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
	
	serializer_class = UserSerializer

	def get_queryset(self):
		queryset = User.objects.all()

		limit = self.request.query_params.get('limit', None)
		name = self.request.query_params.get('name', None)
		sort = self.request.query_params.get('sort', None)
		
		if name:
			query1 = queryset.filter(first_name__contains=name)
			query2 = queryset.filter(last_name__contains=name)

			queryset = query1 | query2
		if sort:
			queryset = queryset.order_by(sort)

		if limit:
			settings.REST_FRAMEWORK['PAGE_SIZE'] = int(limit)

		return queryset