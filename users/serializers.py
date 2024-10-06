from rest_framework.serializers import ModelSerializer  # type: ignore

from users.models import User, Payment


class UserSerializer(ModelSerializer):
    """
    сериализатор модели пользователя
    """

    class Meta:
        model = User
        fields = "__all__"

class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
