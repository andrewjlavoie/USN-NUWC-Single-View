import pymongo
import pandas as pd

# Step 0. Reading in the data and MongoDB Client Connection

employee_to_contracts = pd.read_csv("./testdatasets/ContractorContractsTestSet.csv")
employee_info = pd.read_csv("./testdatasets/ContractorEmployeeTestSet.csv")
contract_info = pd.read_csv("./testdatasets/ContractorTestSet.csv")

client = pymongo.MongoClient('localhost', 27017)
#client = pymongo.MongoClient('mongodb://localhost:27017/')

# Step 1. Creating the Contracts Collection

collection = client['nuwc_singleview']['contracts']
documents = []

for index, row in contract_info.iterrows():
    doc = {}
    doc['_id'] = row['Contract Number']
    doc['contract_owner'] = {
        'name': row['COR Name'],
        'dept_num': row['COR Dept. Number'],
        'email_address': row['COR E-mail Address']
    }
    employees_assigned = employee_to_contracts.loc[
        employee_to_contracts['Contract/Order Number (assigned to)'] == row['Contract Number'], 'Contractor Employee Name'
        ].tolist()
    
    employees_code = []
    for employee in employees_assigned:
        code = employee_to_contracts.loc[
            employee_to_contracts['Contractor Employee Name'] == employee, 'Supporting Code'
            ].values[0]
        employees_code.append({
            'name': employee,
            'supporting_code': code
        })

    doc['employees_assigned'] = employees_code
    documents.append(doc)

collection.insert_many(documents)

# Step 2. Creating the Employees Collection

collection = client['nuwc_singleview']['employees']
documents = []

for index, row in employee_info.iterrows():
    doc = {}
    doc['employee name'] = row['Contractor Employee Name']
    doc['email_address'] = row['Contractor Employee E-mail']
    doc['nmci_account_status'] = row['NMCI Account Status (active, inactive, deleted)']
    doc['badged'] = row['Badged (Yes/No)']
    documents.append(doc)

collection.insert_many(documents)