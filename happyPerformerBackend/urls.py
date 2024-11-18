from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import task_list,task_detail, task_search

urlpatterns = [
    path('', views.Home, name='home'),
    path('meet-the-team/', views.MeetTheTeam, name='meet-the-team'),
    path('contact/', views.Contact, name='contact'),
    path('about/', views.About, name='about'),
    path('login/', views.Login, name='login'),
    path('Users/', views.Users, name='Users'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.Register, name='register'),
    path('TermsAndConditions/', views.TermsAndConditions, name='terms'),
    path('SopAndPolicies/', views.SopAndPolicies, name='soppolicies'),
    path('UpdateSelfratings/<int:sop_id>', views.UpdateSelfratings, name='UpdateSelfratings'),
    path('Forms/', views.Forms, name='Forms'),
    path('FormReviewRespose/', views.FormReviewRespose, name='FormReviewRespose'),
    path('FormsSubmitResponse/', views.FormsSubmitResponse, name='FormsSubmitResponse'),
    path('Kra/', views.KraList, name='KraList'),
    path('Letters/', views.Letters1, name='Letters1'),
    path('FAQsView/', views.FAQsView, name='FAQsView'),
    path('ApplyLeave/', views.ApplyLeave, name='ApplyLeave'),
    path('LeaveHistory/', views.LeaveHistory, name='LeaveHistory'),
    path('AddLoan', views.AddLoan, name='AddLoan'),
    path('AddExpenses', views.AddExpenses, name='AddExpenses'),
    path('ManageExpenses/', views.ManageExpenses, name='ManageExpenses'),
    path('ExpenseReport', views.ExpenseReport, name='ExpenseReport'),
    path('Resign/', views.Resign, name='Resign'),
    path('AddCourses/', views.AddCourses, name='AddCourses'),
    path('UploadMedia/', views.UploadMedia, name='UploadMedia'),
    path('UploadPdf/', views.UploadPdf, name='UploadPdf'),
    path('AddMediaContent/', views.AddMediaContent, name='AddMediaContent'),
    path('UpdateDeleteMedia/', views.UpdateDeleteMedia, name='UpdateDeleteMedia'),
    path('UpdateMedia/<int:course_id>', views.UpdateMedia, name='UpdateMedia'),
    path('ReportingStructureForm/', views.ReportingStructureForm, name='ReportingStructureForm'),
    path('CeoHrAnnouncements/', views.CeoHrAnnouncements, name='CeoHrAnnouncements'),
    path('AddNewEmployee/', views.AddNewEmployee, name='AddNewEmployee'),
    path('UpdateDeleteEmployee/', views.UpdateDeleteEmployee, name='UpdateDeleteEmployee'),
    path('UpdateEmployeeDetails/', views.UpdateEmployeeDetails, name='UpdateEmployeeDetails'),
    path('LeaveDashboard/', views.LeaveDashboard, name='LeaveDashboard'),
    path('LeaveDetails/<int:id>/', views.LeaveDetails, name='LeaveDetails'),
    path('ManageLeaveType/', views.ManageLeaveType, name='ManageLeaveType'),
    path('EditLeaveType/<int:id>/', views.EditLeaveType, name='EditLeaveType'),
    path('Leaves/', views.Leaves, name='Leaves'),
    path('PendingLeaves/', views.PendingLeaves, name='PendingLeaves'),
    path('ApprovedLeaves/', views.ApprovedLeaves, name='ApprovedLeaves'),
    path('RejectedLeaves/', views.RejectedLeaves, name='RejectedLeaves'),
    path('AllResignation/', views.AllResignation, name='AllResignation'),
    path('AllExitClearance/', views.AllExitClearance, name='AllExitClearance'),
    path('AllFinalSettlement/', views.AllFinalSettlement, name='AllFinalSettlement'),
    path('EditResignation/', views.EditResignation, name='EditResignation'),
    path('EditExitClearnace/', views.EditExitClearnace, name='EditExitClearnace'),
    path('GenerateFnf/', views.GenerateFnf, name='GenerateFnf'),

    path('DisplayTraining/', views.DisplayTraining, name='DisplayTraining'),
    path('CreateCase', views.CreateCase, name='CreateCase'),
    path('MyCases', views.MyCases, name='MyCases'),

    path('DisplayTraining', views.DisplayTraining, name='DisplayTraining'),
    path('CreateCase/', views.CreateCase, name='CreateCase'),
    path('MyCases/', views.MyCases, name='MyCases'),
    path('UpdatePersonalDetails/', views.UpdatePersonalDetails, name='UpdatePersonalDetails'),
    path('UpdateJobDetails/', views.UpdateJobDetails, name='UpdateJobDetails'),
    path('UpdateBankDetails/', views.UpdateBankDetails, name='UpdateBankDetails'),
    path('UpdateWorkExperience/', views.UpdateWorkExperience, name='UpdateWorkExperience'),
    path('UpdateAdhaar/', views.UpdateAdhaar, name='UpdateAdhaar'),
    path('UpdateLicence/', views.UpdateLicence, name='UpdateLicence'),
    path('UpdatePassport/', views.UpdatePassport, name='UpdatePassport'),
    path('UpdatePan/', views.UpdatePan, name='UpdatePan'),
    path('UpdateQualification/', views.UpdateQualification, name='UpdateQualification'),
    path('UpdateFamilyDetails/', views.UpdateFamilyDetails, name='UpdateFamilyDetails'),
    path('AllCases/', views.AllCases, name='AllCases'),
    path('CaseInfo/', views.CaseInfo, name='CaseInfo'),
    path('BenefitsCases/', views.BenefitsCases, name='BenefitsCases'),
    path('TravelExpenseCases/', views.TravelExpenseCases, name='TravelExpenseCases'),
    path('CompensationPayrollCases/', views.CompensationPayrollCases, name='CompensationPayrollCases'),
    # path('ManagerRating', views.ManagerRating, name='ManagerRating'),
    path('FAQManagement/', views.FAQManagement, name='FAQManagement'),
    path('EnrollEmployee/', views.EnrollEmployee, name='EnrollEmployee'),
    path('ViewAllEnrollments/', views.ViewAllEnrollments, name='ViewAllEnrollments'),
    path('AdhocPayments/', views.AdhocPayments, name='AdhocPayments'),
    path('LoanPayments/', views.LoanPayments, name='LoanPayments'),
    path('LeaveEncashments/', views.LeaveEncashment, name='LeaveEncashment'),
    path('ViewLeaveEncashment/', views.ViewLeaveEncashment, name='ViewLeaveEncashment'),
    # path('ViewEmployeeEncashment/<str:emp_emailid>/', views.ViewEmployeeEncashment, name='view_employee_encashment'),
    path('OffCyclePayments/', views.OffCyclePayments, name='OffCyclePayments'),
    path('BankTransferPayout/', views.BankTransferPayout, name='BankTransferPayout'),
    path('BankTransfer/', views.BankTransfer, name='BankTransfer'),
    path('BankTransferUpdate/', views.BankTransferUpdate, name='BankTransferUpdate'),
    path('CashChequeTransferPayout/', views.CashChequeTransferPayout, name='CashChequeTransferPayout'),
    path('HoldSalaryPayout/', views.HoldSalaryPayout, name='HoldSalaryPayout'),
    path('HoldSalary/', views.HoldSalary, name='HoldSalary'),
    path('UnholdSalary/', views.UnholdSalary, name='UnholdSalary'),
    path('PayslipPayout/', views.PayslipPayout, name='PayslipPayout'),
    path('GeneratePayslip/', views.GeneratePayslip, name='GeneratePayslip'),
    path('HomeSalary/', views.HomeSalary, name='HomeSalary'),
    path('AddSalary/', views.AddSalary1, name='AddSalary'),
    path('SalaryRevisionHistory/', views.SalaryRevisionHistory, name='SalaryRevisionHistory'),
    path('DisplaySalaryDetails/', views.DisplaySalaryDetails, name='DisplaySalaryDetails'),
    path('CustomForms/', views.CustomForms, name='CustomForms'),
    path('EditFormView/', views.EditFormView, name='EditFormView'),
    path('AllocateFormView/', views.AllocateFormView, name='AllocateFormView'),
    path('AddTextQuestionFormView/', views.AddTextQuestionFormView, name='AddTextQuestionFormView'),
    path('AddRadioQuestionView/', views.AddRadioQuestionView, name='AddRadioQuestionView'),
    path('CustomLetter/', views.CustomLetter, name='CustomLetter'),
    path('EditLetterView/', views.EditLetterView, name='EditLetterView'),
    path('EmployeeDetails/', views.EmployeeDetails, name='EmployeeDetails'),
    path('AttendanceDetails/', views.AttendanceDetails, name='AttendanceDetails'),
    path('EmployeeMaster/', views.EmployeeMaster, name='employeemaster'),
    #added
    path('socialget/', views.social_submit_feedback_get, name='social_submit_feedback_get'),
    path('socialpost/', views.social_submit_feedback_post, name='social_submit_feedback_post'),
    path('socialreact/<int:feedback_id>/', views.social_add_reaction, name='social_add_reaction'),
    path('employee_view/', views.employee_view, name='employee_view'),
    path('getcourses/', views.GetCourses, name='GetCourses'),
    path('allquiz/', views.allquiz, name='allquiz'),
    path('markattendance/', views.markattendance, name='markattendance'),
    path('settings_account/', views.update_settings_account, name='settings_account'),
    path('settings_password/', views.update_settings_password, name='settings_password'),
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('resetpassword/', views.reset_password, name='reset_password'),
    path('LeaveDetails/update_status/<int:leave_id>/', views.update_leave_status, name='update_leave_status'),
    path('EmployeeMaster/<str:emp_emailid>/', views.employee_details, name='employee-details'),
    path('calendar/', views.event_handler, name='event_handler'),
    path('investment-80C/', views.investment_80C, name='investment_80c'),
    path('investment-80D/', views.investment_80D, name='investment_80d'),
    path('other-investments/', views.other_investments, name='other_investments'),
    path('other-income/', views.other_income, name='other_income'),
    path('tasks/', views.task_list1, name='task_list1'),
    path('tasks/<int:task_id>/', views.task_delete, name='task_delete'),
    path('taskss/<int:task_id>/', views.task_update, name='task_update'),
    path('attrition/year/', views.attrition_year_data, name='attrition-year-data'),
    path('attrition/department/', views.attrition_department_data, name='attrition-department-data'),
    path('attrition/reasons/', views.attrition_reason_data, name='attrition-reasons-data'),
    path('attrition/gender/', views.attrition_gender_data, name='attrition-gender-data'),
    path('attrition/choice/', views.attrition_choice_data, name='attrition-choice-data'),
    path('poi/<str:emp_emailid>/', views.poi_list_create, name='poi_list_create'),  # Handles GET and POST requests
    path('poi/<int:poi_id>/', views.poi_delete, name='poi_delete'),

    # path('Settings/', views.Settings, name='Settings'),    
 # path('Settings/UpdateEmployeePassword/', views.UpdateEmployeePassword, name='UpdateEmployeePassword'),
#  added dipayan
    path('ToggleQuizStatus/', views.ToggleQuizStatus, name='ToggleQuizStatus'),
    path('GetAllQuizzes/', views.GetAllQuizzes, name='GetAllQuizzes'),
    path('jdform/', views.JDForm, name='JDForm'),
    # path('markAttendance/', views.MarkAttendance, name='MarkAttendance'),
    path('kraform/', views.KRAForm, name='KRAForm'),
    path('sopform/', views.SOPForm, name='SOPForm'),
    path('bulkUploadEmployeeDetailsUpload/', views.bulkUploadEmployeeDetailsUpload, name='bulkUploadEmployeeDetailsUpload'),
    # path('bulkEmployeeregistration/', views.bulkEmployeeregistration, name='bulkEmployeeregistration'),
    path('SopList/', views.SopList, name='SopList'),
    path('Jdlist/', views.JdList, name='JdList'),
    path('JdDetails/', views.JdDetails, name='JdDetails'),
    path('UpdateDependent/', views.UpdateDependent, name='UpdateDependent'),
    path('CreateQuiz/', views.CreateQuiz, name='CreateQuiz'),
    path('AttemptQuiz/', views.AttemptQuiz, name='AttemptQuiz'),
    path('AttemptQuiz/<int:quiz_id>/', views.AttemptQuiz, name='AttemptQuiz'),
    path('QuizResults/', views.QuizResults, name='QuizResults'),
    path('QuizResults/<int:quiz_id>/', views.QuizResults, name='QuizResults'),
    path('DetailedDescription/<int:quiz_id>/', views.DetailedDescription, name='DetailedDescription'),
    path('AttemptedQuizzes/', views.AttemptedQuizzes, name='AttemptedQuizzes'),
    path('getcomp/', views.get_departments_by_company, name='get_departments_by_company'),
    path('getemp/', views.get_employee_names_by_company, name='get_employee_names_by_company'),
    path('AddBankDetails/', views.AddBankDetails, name='AddBankDetails'),
    path('AddPersonalDetails/', views.AddPersonalDetails, name='AddPersonalDetails'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/', task_detail, name='task_detail'),
    path('tasks/search/', task_search, name='task_search'),
    path('myperformance/<str:employee_email>/<int:year>/', views.get_performance_data, name='get_performance_data'),
    path('jd-form/', views.jd_form, name='jd_form'),
    path('myperformance/<int:year>/', views.get_performance_data, name='get_performance_data'),
    path('benefits-cases/', views.BenefitsCases, name='benefits_cases'),
    path('travel-expense-cases/', views.TravelExpenseCases, name='travel_expense_cases'),
    path('compensation-payroll-cases/', views.CompensationPayrollCases, name='compensation_payroll_cases'),
    path('poitoggle/<str:emp_id>/<str:investment_field>/', views.toggle_investment_status, name='toggle_investment_status'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)