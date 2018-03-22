from rest_framework import serializers

from ..models import User

# Serializer class used for validating user data & convert it to json
class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = (
			'id',
			'first_name',
			'last_name',
			'company_name',
			'age',
			'city',
			'state',
			'zip',
			'email',
			'web'
		)
