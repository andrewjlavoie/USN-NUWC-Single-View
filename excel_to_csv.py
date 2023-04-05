import pandas as pd

f1 = pd.read_excel("./testdatasets/ContractorContractsTestSet.xlsx")
f2 = pd.read_excel("./testdatasets/ContractorEmployeeTestSet.xlsx")
f3 = pd.read_excel("./testdatasets/ContractTestSet.xlsx")

f1.to_csv("./testdatasets/ContractorContractsTestSet.csv", index=None, header=True)
f2.to_csv("./testdatasets/ContractorEmployeeTestSet.csv", index=None, header=True)
f3.to_csv("./testdatasets/ContractorTestSet.csv", index=None, header=True)