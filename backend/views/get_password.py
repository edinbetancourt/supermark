# DRF 
from rest_framework import generics, status
from rest_framework.response import Response

# Serializer
from backend.serializers.get_password import GetPasswordSerializer

# Utils
from backend.utils.derive_password import DerivePassword


class GetPasswordView(generics.GenericAPIView):
    """ Returns the password """

    serializer_class = GetPasswordSerializer

    def get(self, request):

        password = DerivePassword().get_password()

        if password:
            return Response({'result': password}, status=status.HTTP_200_OK)
        else:
            return Response({'result': "Can't open keylog file"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
