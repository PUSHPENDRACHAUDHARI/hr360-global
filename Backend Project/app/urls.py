from django.urls import path, include
from . import views

from .views import create_project_manager

urlpatterns = [

    #----------------------------------------------------------------------------------
    
    ########################### Role Based Access Control URLs #########################
     path('', views.login_view, name='login'),
     path('logout/', views.logout_view, name='logout'),
     path('logout-confirmation/', views.logout_confirmation, name='logout_confirmation'),
    ###################### Dashboard URLs ###############################
     path('dashboard/', views.hr_dashboard, name='hr-dashboard'),
     path('employee-dashboard/', views.employee_dashboard, name='employee-dashboard'),
    #  -------------------------------------------------------------------------------------
    ################################ Employee Module URLs ################################
     path('employee-attendance/', views.employee_attendance, name='employee-attendance'),
     path('employee-attendance-records/', views.employee_attendance_records_simple, name='employee-attendance-records'),
     path('apply-leave/', views.employee_apply_leave, name='apply-leave'),
     path('payslip/', views.employee_payslip, name='payslip'),
     path('employee-profile/', views.employee_profile, name='employee-profile'),
     path('employee-project-dashboard/', views.employee_project_dashboard, name='employee-project-dashboard'),

     path('hr-profile/', views.hr_profile, name='hr-profile'),
     path('tl-profile/', views.tl_profile, name='tl-profile'),
     path('employee-attendance-page/', views.employee_attendance_page, name='employee-attendance-page'),
     path('hr-attendance-page/', views.hr_attendance_page, name='hr-attendance-page'),

    ################################ End Employee Module Url #############################
    # ----------------------------------------------------------------------------------------
    ################################ TL Modules Urls #####################################
     path('tl-dashboard/', views.tl_dashboard, name='tl-dashboard'),
     path('tl-reports/', views.tl_reports, name='tl-reports'),
     path('team-attendence/',views.tl_attendance, name='team-attendence'),
     path('team-leave-approval/', views.team_leave_approval, name='team-leave-approval'),
     path('tl-manage-team/', views.tl_manage_team, name='tl-manage-team'),
     path('tl-project-dashboard/', views.tl_project_dashboard, name='tl-project-dashboard'),

    
    ################################ TL Module Urls End ###################################
    


     path('employee/', views.employee , name='employee-management'),
     path("export-employees/", views.export_employees, name="export-employees"),
     path("show-all-employee/", views.show_all_employees, name="show-all-employee"),
     path("get-employee/<int:emp_id>/", views.get_employee, name="get_employee"),   
     path("delete-employee/<int:emp_id>/", views.delete_employee, name="delete-employee"),
     path("team/", views.team_page, name="team-page"),                     
     path("create-team-leader/", views.create_team_leader, name="create-tl"),
     path("assign-member-page/", views.assign_member_page, name="assign-member-page"),
     path("assign-member-submit/", views.assign_member_submit, name="assign-member-submit"),
     path("update-team-member/", views.tl_manage_team, name="update-team-member"),
     # path("remove-team-member/", views.remove_team_member, name="remove-team-member"),  # Function not implemented
     path("assign-project-page/", views.assign_project_page, name="assign-project-page"),
     path("assign-project-submit/", views.assign_project_submit, name="assign-project-submit"),
     path("get-team-members/", views.get_team_members, name="get-team-members"),
     path('team-info/', views.team_table, name='team-info'),
     path("team-leader/details/<int:tl_id>/", views.get_team_leader_details, name="tl-details"),
     path("delete-team-leader/<int:tl_id>/", views.delete_team_leader, name="delete-tl"),
     

     ############################## HR Management Urls ##########################################
    

     path('attendance/', views.hr_attendance_simple , name='attendance'),
     path('hr-attendance/', views.hr_attendance_simple , name='hr-attendance'),
     path('leave-approvals/', views.leave_approvals, name='leave-approvals'),

     ############################## Employee Payroll MAnagement Urls ##############################

     path('payroll/', views.payroll, name='payroll-management'),
     path("payroll-records/", views.payroll_records, name="payroll-records"),
     path("export-payroll/", views.export_payroll, name="export-payroll"),
     path("delete-payroll/", views.delete_payroll, name="delete-payroll"),   

     path('reports/', views.reports, name='hr-reports'),
     path("api/payroll-data/", views.get_payroll_data, name="payroll-data"),
     path('announcements/', views.announcements, name='hr-announcements'),
     
     # Announcement Management URLs
     path('announcements/view/<int:announcement_id>/', views.view_announcement, name='view-announcement'),
     path('announcements/edit/<int:announcement_id>/', views.edit_announcement_view, name='edit-announcement'),
     path('announcements/update/<int:announcement_id>/', views.update_announcement, name='update-announcement'),
     path('announcements/delete/<int:announcement_id>/', views.delete_announcement, name='delete-announcement'),
     
     # path('team/', views.team, name='hr-team'), # Commented out duplicate


     ######################################## HR Management URLs ####################
     path('create-hr/', views.hr_create, name='create-hr'),
     path('hr-list/', views.hr_list, name='hr-list'),
     path('delete-hr/<int:hr_id>/', views.delete_hr, name='delete-hr'),
     
     # Test leave management system
     path('test-leave-system/', views.test_leave_system, name='test-leave-system'),

    # ============================================================================
    # NEW PAYROLL & ATTENDANCE MANAGEMENT URLs
    # ============================================================================

    # Employee Attendance URLs
    path('employee-check-in/', views.employee_attendance_simple, name='employee-check-in'),
    path('employee-check-out/', views.employee_check_out, name='employee-check-out'),

    # Team Leader Attendance Management URLs
    path('tl-attendance-management/', views.tl_attendance_management, name='tl-attendance-management'),

    # HR Monthly Attendance Summary URLs
    path('hr-monthly-attendance-summary/', views.hr_monthly_attendance_summary, name='hr-monthly-attendance-summary'),

    # HR Payroll Calculations URLs
    path('hr-payroll-calculations/', views.hr_payroll_calculations, name='hr-payroll-calculations'),


    path('payroll-emp/', views.payrollemployeepage, name='payroll-emp'),
    #  -------------------------------------------------------------------------------------------
    ################################## Team Lead Management URLs ####################################
    # --------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
   ################################### Project Manager Urls #########################################
    # -----------------------------------------------------------------------------------------------
    path("project-manager-profile/", views.create_project_manager, name="create-project-manager"),
    path("project-manager-dashboard/",views.pm_dashboard, name="project-manager-dashboard"),
    path('pm/logout/', views.project_manager_logout, name='pm-logout'),
    path('pm/confirm-logout/', views.project_manager_confirm_logout, name='pm-confirm-logout'),
    path('pm/<str:pm_id>/profile/',views.project_manager_profile,name='project-manager-profile'),
    path('clients/', views.client_management, name='client-management'),
    path('clients/delete/<int:id>/', views.client_delete, name='client-delete'),
    path("pm/projects/", views.pm_projects, name="pm-projects"),
    path("pm/team_lead_profile/<int:lead_id>/", views.team_lead_profile, name="team-lead-profile"),
    path("pm/team-lead/<int:lead_id>/details/",views.team_lead_details,name="team-lead-details"),
    path('pm/teams/', views.pm_teams, name='pm-teams'),
    path('pm/team/view/<int:id>/', views.team_view, name='team-view'),
    path('pm/team/edit/<int:id>/', views.team_edit, name='team-edit'),
    path('pm/team/delete/<int:id>/', views.team_delete, name='team-delete'),
    path('pm/leave-manage/',views.pm_leave_manage,name='pm-leave-manage'),
    path('pm/leave/<int:id>/',views.pm_leave_view,name='pm-leave-view'),
    path('pm/reports/', views.pm_reports, name='pm-reports'),

]

