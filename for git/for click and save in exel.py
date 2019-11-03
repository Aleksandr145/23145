from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Name"
sheet["C1"] = "phone"
sheet["D1"] = "all"
sheet["M1"] = "advancer"

workbook.save(filename="hello_world.xlsx")

input("All Done")
