from payments.models import User
from rest_framework import serializers
import random
import string
import uuid

class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField(required=False)
    status = serializers.CharField(default='nonactive')

    def generate_random_username(self):
        # Generate a random username using a combination of letters and digits
        length = 8
        letters_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_digits) for _ in range(length))

    def create(self, validated_data):
        if 'username' not in validated_data:
            validated_data['username'] = self.generate_random_username()
        return User.objects.create(uuid=uuid.uuid4(), **validated_data)
    
    def update(self, instance, validated_data):
        # Disable updating the user_id field
        validated_data.pop('user_id', None)
        return super().update(instance, validated_data)
    
    def validate_user_id(self, value):
        if value <= 0:
            raise serializers.ValidationError("User ID must be a positive integer.")
        # Validate uniqueness of user_id
        if User.objects.filter(user_id=value).exists():
            raise serializers.ValidationError("user_id already saved")
        return value

    class Meta:
        model = User
        fields = ('id', 'uuid', 'user_id', 'username', 'status', 'created_at', 'updated_at')
        read_only_fields = ('uuid', 'id', 'created_at', 'updated_at')