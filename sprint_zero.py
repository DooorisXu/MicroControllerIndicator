import xlrd
import easygui

path = "/Users/a01/Desktop/MagicStuff/PycharmProjects/summer@brown/prescription.xlsm"
prescription = xlrd.open_workbook(path)
sheet_prescription = prescription.sheets()[0]
sheet_index = prescription.sheets()[1]
rowCount = int(sheet_index.cell_value(rowx=1,colx=0))
print(rowCount)
reminder = {}
for i in range (1, rowCount+1):
    r = sheet_prescription.row_values(i)
    reminder = reminder + r

easygui.msgbox(reminder, title = "Today's Reminders")
print(reminder)





