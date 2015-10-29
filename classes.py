class Visit:
    visitList = {}

    def __init__(self, date, cost, idNum=None):
        if idNum == None:
            self.idNum = len(Visit.visitList) + 1
        else:
            self.idNum = idNum
        self.date = date
        self.cost = cost
        self.doctor = None

        Visit.visitList[self.idNum] = self

    def addDoctor(self, doctor):
        self.doctor = doctor

class Doctor:
    doctorList = {}

    def __init__(self, name, startDate, endDate=None, idNum=None):
        if idNum == None:
            self.idNum = len(Doctor.doctorList.keys()) + 1
        else:
            self.idNum = idNum
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.diagnoses = []
        self.testsRun = []
        self.treatmentsRx = []
        self.visits = []

        Doctor.doctorList[self.idNum] = self

    def addVisit(self, visit):
        self.visits.append(visit)

    def addCondition(self, condition):
        self.diagnoses.append(condition)

    def addTreatment(self, treatment):
        self.treatmentsRx.append(treatment)

    def addTest(self, test):
        self.testsRun.append(test)

class Condition:
    conditionList = {}
    statusList = ("Confirmed", "Disconfirmed", "Preliminary", "Cured")

    def __init__(self, name, status, startDate, endDate, notes, idNum=None):
        if idNum == None:
            self.idNum = len(Condition.conditionList.keys()) + 1
        else:
            self.idNum = idNum
        self.name = name
        if status not in Condition.statusList:
            self.status = "Preliminary"
        else:
            self.status = status

        self.startDate = startDate
        self.endDate = endDate
        self.notes = notes
        self.diagnosingDr = None
        self.symptoms = []
        self.treatments = []
        self.tests = []

        Condition.conditionList[self.idNum] = self

    def addDoctor(self, doctor):
        self.diagnosingDr = doctor

    def addSymptom(self, symptom):
        self.symptoms.append(symptom)

    def addTreatment(self, treatment):
        self.treatments.append(treatment)

    def addTest(self, test):
        self.tests.append(test)

class Test:
    testList = {}

    def __init__(self, name, dateTaken, cost, notes, filePath, idNum=None):
        if idNum == None:
            self.idNum = len(Test.testList.keys()) + 1
        else:
            self.idNum = idNum
        self.name = name
        self.date = dateTaken
        self.cost = cost
        self.notes = notes
        self.file = filePath
        self.forCondition = None
        self.doctor = None

        Test.testList[self.idNum] = self

    def addCondition(self, condition):
        self.forCondition = condition

    def addDoctor(self, doctor):
        self.doctor = doctor

class Symptom:
    symptomList = {}

    def __init__(self, name, idNum=None):
        if idNum == None:
            self.idNum = len(Symptom.symptomList.keys()) + 1
        else:
            self.idNum = idNum
        self.name = name
        self.occurrences = []

        Symptom.symptomList[self.idNum] = self

    def addOccurrence(self, symptomOccurrence):
        self.occurrences.append(symptomOccurrence)

class SymptomOccurrence:
    symptomOccurrenceList = {}

    def __init__(self, date, idNum=None):
        if idNum == None:
            self.idNum = len(SymptomOccurrence.symptomOccurrenceList.keys()) + 1
        else:
            self.idNum = idNum
        self.date = date
        self.occurrenceOf = None

    def addOccurrenceOf(self, symptom):
        self.occurrenceOf = symptom

class Treatment:
    treatmentList = {}

    def __init__(self, name, dosageUnit, cost, idNum=None):
        if idNum == None:
            self.idNum = len(Treatment.treatmentList.keys()) + 1
        else:
            self.idNum = idNum
        self.name = name
        self.dosageUnit = dosageUnit
        self.cost = cost
        self.forCondition = None
        self.doctor = None
        self.treatmentDetails = []

        Treatment.treatmentList[self.idNum] = self

    def addCondition(self, condition):
        self.forCondition = condition

    def addDoctor(self, doctor):
        self.doctor = doctor

    def addDetail(self, treatmentDetail):
        self.treatmentDetails.append(treatmentDetail)

class TreatmentDetail:
    treatmentDetailList = {}

    def __init__(self, dosage, date, idNum=None):
        if idNum == None:
            self.idNum = len(TreatmentDetail.treatmentDetailList.keys()) + 1
        else:
            self.idNum = idNum
        self.dosage = dosage
        self.date = date
        self.detailOf = None

        TreatmentDetail.treatmentDetailList[self.idNum] = self

    def addDetailOf(self, treatment):
        self.detailOf = treatment

class Patient:
    patientList = {}

    def __init__(self, name, idNum=None):
        if idNum == None:
            self.idNum = len(Patient.patientList.keys()) + 1
        else:
            self.idNum = idNum
        self.name = name
        self.conditions = []
        self.symptoms = []
        self.tests = []
        self.treatments = []

        Patient.patientList[self.idNum] = self

    def addCondition(self):
        self.conditions.append(Condition())

class Hierarchy:
    def __init__(self):
        self.doctors = {}
        self.conditions = {}
        self.treatments = {}
        self.treatmentsDetails = {}
        self.symptoms = {}
        self.symptomsOccurrences = {}
        self.tests = {}
        self.visits = {}
