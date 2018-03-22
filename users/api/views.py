# Built in import
from rest_framework import generics
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework import status

# App import
from ..models import User
from .serializers import UserSerializer

# for listing and creating user data
class UserListCreateView(generics.ListCreateAPIView):
	
	serializer_class = UserSerializer

	def get_queryset(self):
		queryset = User.objects.all()

		# getting all the parameters
		limit = self.request.query_params.get('limit', None)
		name = self.request.query_params.get('name', None)
		sort = self.request.query_params.get('sort', None)
		
		# if name parameter is present then filter the queryset
		if name:
			query1 = queryset.filter(first_name__contains=name)
			query2 = queryset.filter(last_name__contains=name)
			queryset = query1 | query2

		# if sort parameter is present then order the queryset
		if sort:
			queryset = queryset.order_by(sort)

		# if limit parameter is present then change page_size
		if limit:
			pagination.PageNumberPagination.page_size = int(limit)

		return queryset


# for retrieving, updating and deleting users data
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = UserSerializer
	lookup_field = 'id'
	queryset = User.objects.all()

	# modifying the destroy method of DestroyModelMixin for 200 OK return
	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)
		return Response(status=status.HTTP_200_OK)