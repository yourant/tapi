#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:urls.py
@time:2021/07/29
@email:xutao@dustess.com
@description:
"""

from django.conf.urls import url

from api_test.api import ApiDoc, automationCase as Case, member, dynamic, user, VisitorRecord, DingManage
from api_test.api import automationReport as Report
from api_test.api.global_parameter import HostTotal, AddHost, UpdateHost, DelHost, DisableHost, EnableHost
from api_test.api.projectList import ProjectGroupList, AddProjectGroup, UpdateProjectGroup, DelProjectGroup, \
    ProjectList, AddProject, DelProject, EnableProject, UpdateProject, DisableProject
from api_test.api.projectTitle import ProjectInfo
from api_test.api.departmentList import DepartmentList
from api_test.api.user import UserList

urlpatterns = [
    url(r'user/dingConfig', DingManage.DingManage.as_view()),
    # url(r'user/dingLogin', DingManage.DingLogin.as_view()),
    # 新增项目分组
    url(r'department/department_list', DepartmentList.as_view()),
    url(r'project/group_list', ProjectGroupList.as_view()),
    url(r'project/add_group', AddProjectGroup.as_view()),
    url(r'project/update_group', UpdateProjectGroup.as_view()),
    url(r'project/del_group', DelProjectGroup.as_view()),

    url(r'project/project_list', ProjectList.as_view()),
    url(r'project/add_project', AddProject.as_view()),
    url(r'project/update_project', UpdateProject.as_view()),
    url(r'project/del_project', DelProject.as_view()),
    url(r'project/disable_project', DisableProject.as_view()),
    url(r'project/enable_project', EnableProject.as_view()),
    url(r'title/project_info', ProjectInfo.as_view()),
    url(r'global/host_total', HostTotal.as_view()),
    url(r'global/add_host', AddHost.as_view()),
    url(r'global/update_host', UpdateHost.as_view()),
    url(r'global/del_host', DelHost.as_view()),
    url(r'global/disable_host', DisableHost.as_view()),
    url(r'global/enable_host', EnableHost.as_view()),
    url(r'api/group', ApiDoc.Group.as_view()),
    url(r'api/add_group', ApiDoc.AddGroup.as_view()),
    url(r'api/update_name_group', ApiDoc.UpdateNameGroup.as_view()),
    url(r'api/del_group', ApiDoc.DelGroup.as_view()),
    url(r'api/api_list', ApiDoc.ApiList.as_view()),
    url(r'api/add_api', ApiDoc.AddApi.as_view()),
    url(r'api/updateMock', ApiDoc.UpdateApiMockStatus.as_view()),
    url(r'api/lead_swagger', ApiDoc.LeadSwagger.as_view()),
    url(r'api/update_api', ApiDoc.UpdateApi.as_view()),
    url(r'api/del_api', ApiDoc.DelApi.as_view()),
    url(r'api/update_group', ApiDoc.UpdateGroup.as_view()),
    url(r'api/api_info', ApiDoc.ApiInfoDetail.as_view()),
    url(r'api/add_history', ApiDoc.AddHistory.as_view()),
    url(r'api/history_list', ApiDoc.HistoryList.as_view()),
    url(r'api/del_history', ApiDoc.DelHistory.as_view()),
    url(r'api/operation_history', ApiDoc.OperationHistory.as_view()),
    url(r'api/Download', ApiDoc.DownLoad.as_view()),
    url(r'api/download_doc', ApiDoc.download_doc),
    url(r'automation/group', Case.Group.as_view()),
    url(r'automation/add_group', Case.AddGroup.as_view()),
    url(r'automation/del_group', Case.DelGroup.as_view()),
    url(r'automation/update_name_group', Case.UpdateNameGroup.as_view()),
    url(r'automation/update_case_group', Case.UpdateGroup.as_view()),
    url(r'automation/case_list', Case.CaseList.as_view()),
    url(r'automation/add_case', Case.AddCase.as_view()),
    url(r'automation/update_case', Case.UpdateCase.as_view()),
    url(r'automation/del_case', Case.DelCase.as_view()),
    url(r'automation/DownloadCase', Case.DownLoadCase.as_view()),
    url(r'automation/api_list', Case.ApiList.as_view()),
    url(r'automation/api_info', Case.CaseApiInfo.as_view()),
    url(r'automation/add_new_api', Case.AddNewApi.as_view()),
    url(r'automation/get_correlation_response', Case.GetCorrelationResponse.as_view()),
    url(r'automation/add_old_api', Case.AddOldApi.as_view()),
    url(r'automation/update_api', Case.UpdateApi.as_view()),
    url(r'automation/del_api', Case.DelApi.as_view()),
    url(r'automation/start_test', Case.StartTest.as_view()),
    url(r'automation/add_time_task', Case.AddTimeTask.as_view()),
    url(r'automation/get_time_task', Case.GetTask.as_view()),
    url(r'automation/del_task', Case.DelTask.as_view()),
    url(r'automation/look_result', Case.LookResult.as_view()),
    url(r'automation/test_report', Case.TestReport.as_view()),
    url(r'report/auto_test_report', Report.AutoTestReport.as_view()),
    url(r'report/test_time', Report.TestTime.as_view()),
    url(r'report/lately_ten', Report.AutoLatelyTenTime.as_view()),
    url(r'member/project_member', member.ProjectMemberList.as_view()),
    url(r'member/email_config', member.EmailConfig.as_view()),
    url(r'member/del_email', member.DelEmail.as_view()),
    url(r'member/get_email', member.GetEmail.as_view()),
    url(r'dynamic/dynamic', dynamic.Dynamic.as_view()),
    url(r'user/login', user.obtain_auth_token),
    url(r'user/VisitorRecord', VisitorRecord.Record.as_view()),
    url(r'user/user_list', UserList.as_view()),
]


if __name__ == '__main__':
    pass
