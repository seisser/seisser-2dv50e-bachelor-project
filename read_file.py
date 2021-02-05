import xlrd
import z3

loc = ("Requirements_gold_and_criteria.xls")
 

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(10)
 

sheet.cell_value(0, 0)
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))

