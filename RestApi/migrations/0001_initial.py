# Generated by Django 2.1.15 on 2021-02-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tbldiarydispatchregister',
            fields=[
                ('registerid', models.IntegerField(db_column='RegisterID', primary_key=True, serialize=False)),
                ('organizationid', models.IntegerField(db_column='OrganizationID')),
                ('departmentid', models.IntegerField(db_column='DepartmentID')),
                ('sectionid', models.IntegerField(db_column='SectionID')),
                ('designationid', models.IntegerField(db_column='DesignationID')),
                ('registertype', models.CharField(db_column='RegisterType', max_length=10)),
                ('registermode', models.CharField(db_column='RegisterMode', max_length=10)),
                ('registeryear', models.CharField(db_column='RegisterYear', max_length=4)),
                ('registermonth', models.CharField(db_column='RegisterMonth', max_length=2)),
                ('subject', models.CharField(blank=True, db_column='Subject', max_length=1000, null=True)),
                ('diarydispatchno', models.CharField(blank=True, db_column='DiaryDispatchNo', max_length=100, null=True)),
                ('diarydispatchdate', models.DateField(blank=True, db_column='DiaryDispatchDate', null=True)),
                ('referenceno', models.CharField(blank=True, db_column='ReferenceNo', max_length=100, null=True)),
                ('priority', models.CharField(blank=True, db_column='Priority', max_length=10, null=True)),
                ('classification', models.CharField(blank=True, db_column='Classification', max_length=10, null=True)),
                ('documentnatureid', models.IntegerField(blank=True, db_column='DocumentNatureID', null=True)),
                ('externaldiarytypeid', models.IntegerField(blank=True, db_column='ExternalDiaryTypeID', null=True)),
                ('externaldiarynumber', models.CharField(blank=True, db_column='ExternalDiaryNumber', max_length=30, null=True)),
                ('correspondingdiaryid', models.IntegerField(blank=True, db_column='CorrespondingDiaryID', null=True)),
                ('officename', models.TextField(blank=True, db_column='OfficeName', null=True)),
                ('remarks', models.CharField(blank=True, db_column='Remarks', max_length=250, null=True)),
                ('assignedpersonto', models.CharField(blank=True, db_column='AssignedPersonTo', max_length=2000, null=True)),
                ('carboncopiesto', models.CharField(blank=True, db_column='CarbonCopiesTo', max_length=2000, null=True)),
                ('workflownos', models.CharField(blank=True, db_column='WorkflowNos', max_length=500, null=True)),
                ('documenturl', models.TextField(blank=True, db_column='DocumentURL', null=True)),
                ('checkregisterwithoutassignment', models.BooleanField(blank=True, db_column='CheckRegisterWithoutAssignment', null=True)),
                ('markto', models.CharField(blank=True, db_column='MarkTo', max_length=100, null=True)),
                ('isactive', models.BooleanField(blank=True, db_column='IsActive', null=True)),
                ('deletereason', models.CharField(blank=True, db_column='DeleteReason', max_length=300, null=True)),
                ('author', models.IntegerField(blank=True, db_column='Author', null=True)),
                ('created', models.DateTimeField(blank=True, db_column='Created', null=True)),
                ('editor', models.IntegerField(blank=True, db_column='Editor', null=True)),
                ('modified', models.DateTimeField(blank=True, db_column='Modified', null=True)),
                ('ldcourtname', models.CharField(blank=True, db_column='LDCourtName', max_length=250, null=True)),
                ('ldcaseno', models.CharField(blank=True, db_column='LDCaseNo', max_length=250, null=True)),
                ('ldsubject', models.CharField(blank=True, db_column='LDSubject', max_length=1000, null=True)),
                ('ldnameofparties', models.CharField(blank=True, db_column='LDNameOfParties', max_length=500, null=True)),
                ('ldconcernedwing', models.CharField(blank=True, db_column='LDConcernedWing', max_length=250, null=True)),
                ('islegal', models.BooleanField(db_column='IsLegal')),
                ('campofficediaryno', models.CharField(blank=True, db_column='CampOfficeDiaryNo', max_length=100, null=True)),
                ('initiatedoffice', models.CharField(blank=True, db_column='InitiatedOffice', max_length=250, null=True)),
                ('initiateddiaryno', models.CharField(blank=True, db_column='InitiatedDiaryNo', max_length=250, null=True)),
                ('directedby', models.CharField(blank=True, db_column='DirectedBy', max_length=250, null=True)),
                ('documentissuedate', models.DateField(blank=True, db_column='DocumentIssueDate', null=True)),
                ('isfilediaryentry', models.BooleanField(blank=True, db_column='IsFileDiaryEntry', null=True)),
                ('workflowno', models.CharField(blank=True, db_column='WorkflowNo', max_length=100, null=True)),
            ],
            options={
                'db_table': 'tblDiaryDispatchRegister',
                'managed': False,
            },
        ),
    ]
