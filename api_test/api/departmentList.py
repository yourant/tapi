#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:departmentList.py
@time:2021/08/01
@email:xutao@dustess.com
@description:
"""

import logging

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

from api_test.common.api_response import JsonResponse
from api_test.models import Department
from api_test.serializers import DepartmentSerializer

logger = logging.getLogger(__name__)  # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。


class DepartmentList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def get(self, request):
        """
        获取部门列表
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
            obi = Department.objects.filter(name__contains=name).order_by("id")
        else:
            obi = Department.objects.all().order_by("id")
        paginator = Paginator(obi, page_size)  # paginator对象
        total = paginator.num_pages  # 总页数
        try:
            obm = paginator.page(page)
        except PageNotAnInteger:
            obm = paginator.page(1)
        except EmptyPage:
            obm = paginator.page(paginator.num_pages)
        serialize = DepartmentSerializer(obm, many=True)
        return JsonResponse(data={"data": serialize.data,
                                  "page": page,
                                  "total": total
                                  }, code="999999", msg="成功")


if __name__ == '__main__':
    pass
