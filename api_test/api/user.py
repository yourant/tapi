#!/usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:TXU
@file:DingConfig.py
@time:2021/07/29
@email:xutao@dustess.com
@description:
"""
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from api_test.serializers import TokenSerializer, UserSerializer
from api_test.common.api_response import JsonResponse
from django.contrib.auth.models import User


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        """
        用户登录
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.serializer_class(data=request.data,
                                           context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        # token, created = Token.objects.get_or_create(user=user)
        data = TokenSerializer(Token.objects.get(user=user)).data
        data["userphoto"] = '/file/userphoto.jpg'
        return JsonResponse(data=data, code="999999", msg="成功")


class UserList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def get(self, request):
        """
        获取User列表
        :param request:
        :return:
        """
        try:
            page_size = int(request.GET.get("page_size", 20))
            page = int(request.GET.get("page", 1))
        except (TypeError, ValueError):
            return JsonResponse(code="999985", msg="page and page_size must be integer!")
        name = request.GET.get("name")
        if name:
            obi = User.objects.filter(name__contains=name).order_by("id")
        else:
            obi = User.objects.all().order_by("id")
        paginator = Paginator(obi, page_size)  # paginator对象
        total = paginator.num_pages  # 总页数
        try:
            obm = paginator.page(page)
        except PageNotAnInteger:
            obm = paginator.page(1)
        except EmptyPage:
            obm = paginator.page(paginator.num_pages)
        serialize = UserSerializer(obm, many=True)
        return JsonResponse(data={"data": serialize.data,
                                  "page": page,
                                  "total": total
                                  }, code="999999", msg="成功")


obtain_auth_token = ObtainAuthToken.as_view()
