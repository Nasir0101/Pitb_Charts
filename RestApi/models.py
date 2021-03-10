from django.db import models


class Tbldiarydispatchregister(models.Model):
    # id = models.AutoField(db_column='ID', unique=True)  # Field name made lowercase.
    registerid = models.IntegerField(db_column='RegisterID', primary_key=True)  # Field name made lowercase.
    organizationid = models.IntegerField(db_column='OrganizationID')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentID')  # Field name made lowercase.
    sectionid = models.IntegerField(db_column='SectionID')  # Field name made lowercase.
    designationid = models.IntegerField(db_column='DesignationID')  # Field name made lowercase.
    registertype = models.CharField(db_column='RegisterType', max_length=10)  # Field name made lowercase.
    registermode = models.CharField(db_column='RegisterMode', max_length=10)  # Field name made lowercase.
    registeryear = models.CharField(db_column='RegisterYear', max_length=4)  # Field name made lowercase.
    registermonth = models.CharField(db_column='RegisterMonth', max_length=2)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    diarydispatchno = models.CharField(db_column='DiaryDispatchNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    diarydispatchdate = models.DateField(db_column='DiaryDispatchDate', blank=True, null=True)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    priority = models.CharField(db_column='Priority', max_length=10, blank=True, null=True)  # Field name made lowercase.
    classification = models.CharField(db_column='Classification', max_length=10, blank=True, null=True)  # Field name made lowercase.
    documentnatureid = models.IntegerField(db_column='DocumentNatureID', blank=True, null=True)  # Field name made lowercase.
    externaldiarytypeid = models.IntegerField(db_column='ExternalDiaryTypeID', blank=True, null=True)  # Field name made lowercase.
    externaldiarynumber = models.CharField(db_column='ExternalDiaryNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    correspondingdiaryid = models.IntegerField(db_column='CorrespondingDiaryID', blank=True, null=True)  # Field name made lowercase.
    officename = models.TextField(db_column='OfficeName', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=250, blank=True, null=True)  # Field name made lowercase.
    assignedpersonto = models.CharField(db_column='AssignedPersonTo', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    carboncopiesto = models.CharField(db_column='CarbonCopiesTo', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    workflownos = models.CharField(db_column='WorkflowNos', max_length=500, blank=True, null=True)  # Field name made lowercase.
    documenturl = models.TextField(db_column='DocumentURL', blank=True, null=True)  # Field name made lowercase.
    checkregisterwithoutassignment = models.BooleanField(db_column='CheckRegisterWithoutAssignment', blank=True, null=True)  # Field name made lowercase.
    markto = models.CharField(db_column='MarkTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    deletereason = models.CharField(db_column='DeleteReason', max_length=300, blank=True, null=True)  # Field name made lowercase.
    author = models.IntegerField(db_column='Author', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    editor = models.IntegerField(db_column='Editor', blank=True, null=True)  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.
    ldcourtname = models.CharField(db_column='LDCourtName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ldcaseno = models.CharField(db_column='LDCaseNo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ldsubject = models.CharField(db_column='LDSubject', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ldnameofparties = models.CharField(db_column='LDNameOfParties', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ldconcernedwing = models.CharField(db_column='LDConcernedWing', max_length=250, blank=True, null=True)  # Field name made lowercase.
    islegal = models.BooleanField(db_column='IsLegal')  # Field name made lowercase.
    campofficediaryno = models.CharField(db_column='CampOfficeDiaryNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    initiatedoffice = models.CharField(db_column='InitiatedOffice', max_length=250, blank=True, null=True)  # Field name made lowercase.
    initiateddiaryno = models.CharField(db_column='InitiatedDiaryNo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    directedby = models.CharField(db_column='DirectedBy', max_length=250, blank=True, null=True)  # Field name made lowercase.
    documentissuedate = models.DateField(db_column='DocumentIssueDate', blank=True, null=True)  # Field name made lowercase.
    # isfilediaryentry = models.BooleanField(db_column='IsFileDiaryEntry', blank=True, null=True)  # Field name made lowercase.
    # workflowno = models.CharField(db_column='WorkflowNo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDiaryDispatchRegister'
        unique_together = (('registerid', 'organizationid', 'departmentid', 'sectionid', 'designationid', 'registertype', 'registermode', 'registeryear', 'registermonth'),)



class Tblorganization(models.Model):
    organizationid = models.IntegerField(db_column='OrganizationID', primary_key=True)  # Field name made lowercase.
    governmentid = models.IntegerField(db_column='GovernmentID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    staticname = models.CharField(db_column='StaticName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    isorganizationbaseregister = models.BooleanField(db_column='IsOrganizationBaseRegister', blank=True, null=True)  # Field name made lowercase.
    iscontaincopyregisterdocument = models.BooleanField(db_column='IsContainCopyRegisterDocument', blank=True, null=True)  # Field name made lowercase.
    isregisterwithoutassignment = models.BooleanField(db_column='IsRegisterWithoutAssignment', blank=True, null=True)  # Field name made lowercase.
    enabledocumentcenter = models.BooleanField(db_column='EnableDocumentCenter', blank=True, null=True)  # Field name made lowercase.
    documentcenterurl = models.CharField(db_column='DocumentCenterURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    author = models.IntegerField(db_column='Author', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    editor = models.IntegerField(db_column='Editor', blank=True, null=True)  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.
    employeenameinnoting = models.BooleanField(db_column='EmployeeNameInNoting', blank=True, null=True)  # Field name made lowercase.
    isbackdatediary = models.BooleanField(db_column='IsBackDateDiary', blank=True, null=True)  # Field name made lowercase.
    enableremarks = models.BooleanField(db_column='EnableRemarks', blank=True, null=True)  # Field name made lowercase.
    webapipath = models.CharField(db_column='WebAPIPath', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    isnotingmandatory = models.BooleanField(db_column='IsNotingMandatory', blank=True, null=True)  # Field name made lowercase.
    scanningserverurl = models.CharField(db_column='ScanningServerURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isiprestriction = models.BooleanField(db_column='IsIPRestriction', blank=True, null=True)  # Field name made lowercase.
    privateipaddress = models.CharField(db_column='PrivateIPAddress', max_length=25, blank=True, null=True)  # Field name made lowercase.
    enablescanning = models.BooleanField(db_column='EnableScanning', blank=True, null=True)  # Field name made lowercase.
    blockincomingdiaryworkflow = models.BooleanField(db_column='BlockIncomingDiaryWorkflow', blank=True, null=True)  # Field name made lowercase.
    sendemailonreister = models.BooleanField(db_column='SendEmailOnReister', blank=True, null=True)  # Field name made lowercase.
    emailwithattachments = models.BooleanField(db_column='EmailWithAttachments', blank=True, null=True)  # Field name made lowercase.
    sendemailtocc = models.BooleanField(db_column='SendEmailToCC', blank=True, null=True)  # Field name made lowercase.
    emailwithphysicalattachment = models.BooleanField(db_column='EmailWithPhysicalAttachment', blank=True, null=True)  # Field name made lowercase.
    diarydispatchnoby = models.IntegerField(db_column='DiaryDispatchNoBy', blank=True, null=True)  # Field name made lowercase.
    restrictimei = models.BooleanField(db_column='RestrictImei')  # Field name made lowercase.
    allowmultforwardwithfileprepared = models.BooleanField(db_column='AllowMultForwardWithFilePrepared')  # Field name made lowercase.
    enablechangepassword = models.BooleanField(db_column='EnableChangePassword', blank=True, null=True)  # Field name made lowercase.
    enablequickresponse = models.BooleanField(db_column='EnableQuickResponse', blank=True, null=True)  # Field name made lowercase.
    helpdesktitle = models.CharField(db_column='HelpDeskTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isfileapprovalrequired = models.BooleanField(db_column='IsFileApprovalRequired', blank=True, null=True)  # Field name made lowercase.
    enablehelpdesk = models.BooleanField(db_column='EnableHelpDesk', blank=True, null=True)  # Field name made lowercase.
    priority = models.CharField(db_column='Priority', max_length=50, blank=True, null=True)  # Field name made lowercase.
    classification = models.CharField(db_column='Classification', max_length=50, blank=True, null=True)  # Field name made lowercase.
    documentnatureid = models.IntegerField(db_column='DocumentNatureID', blank=True, null=True)  # Field name made lowercase.
    enabledocumentnatureatregister = models.BooleanField(db_column='EnableDocumentNatureAtRegister', blank=True, null=True)  # Field name made lowercase.
    addressline1 = models.CharField(db_column='AddressLine1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='AddressLine2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    addressline3 = models.CharField(db_column='AddressLine3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enablemeetingnoticeasvcalendar = models.BooleanField(db_column='EnableMeetingNoticeAsVCalendar', blank=True, null=True)  # Field name made lowercase.
    enablemeetingreminder = models.BooleanField(db_column='EnableMeetingReminder', blank=True, null=True)  # Field name made lowercase.
    remindertime = models.IntegerField(db_column='ReminderTime', blank=True, null=True)  # Field name made lowercase.
    enablecumulativemeetings = models.BooleanField(db_column='EnableCumulativeMeetings', blank=True, null=True)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dbusername = models.CharField(db_column='DBUserName', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    dbpassword = models.CharField(db_column='DBPassword', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    enablecrossorgwithregister = models.BooleanField(db_column='EnableCrossOrgWithRegister', blank=True, null=True)  # Field name made lowercase.
    mainsiteurl = models.CharField(db_column='MainSiteURL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    isdatabasesplit = models.BooleanField(db_column='IsDatabaseSplit', blank=True, null=True)  # Field name made lowercase.
    enablebackdatemeeting = models.BooleanField(db_column='EnableBackDateMeeting', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOrganization'