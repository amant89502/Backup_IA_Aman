import xlwings as xw

# Connect to the source Excel file
source_file_path = "C:/Users/158173/OneDrive - Arrow Electronics, Inc/Documents/aman_excel1.xlsx"
source_wb = xw.Book(source_file_path)

# Get the active sheet of the source workbook
source_sheet = source_wb.sheets.active

# Connect to the destination Excel file
destination_file_path = "C:/Users/158173/OneDrive - Arrow Electronics, Inc/Documents/amanexcel2.xlsx"
destination_wb = xw.Book(destination_file_path)

# Get the active sheet of the destination workbook
destination_sheet = destination_wb.sheets.active

# Copy data from source sheet to destination sheet
source_range = source_sheet.range('A1').expand('table')  # Adjust the range as needed
source_data = source_range.value
destination_sheet.range('A1').value = source_data

# Close the source workbook (if desired)
source_wb.close()


# Save and close the destination workbook
destination_wb.save()
destination_wb.close()

print("Data copied successfully!")
