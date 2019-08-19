from django.contrib.auth import get_user_model, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


User = get_user_model()


@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    """
    A view that handles authentication process and returns an authentication
    token for authenticated users
    :param request:
    :return error or token if user is authenticated:
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response(
            {'error': _("Please provide both username and password"), },
            status=HTTP_400_BAD_REQUEST
        )
    user = authenticate(username=username, password=password)
    if not user:
        return Response(
            {'error': _("Invalid credentials"), },
            status=HTTP_404_NOT_FOUND
        )
    token, created = Token.objects.get_or_create(user=user)
    return Response(
        {'token': token.key, },
        status=HTTP_200_OK
    )


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
