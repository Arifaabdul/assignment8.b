
# Exlore in google and create a document.

# 1. What is excel file ?
'''Excel is a spreadsheet program from Microsoft and a component of its Office product group for business applications. 
Microsoft Excel enables users to format, organize and calculate data in a spreadsheet.'''

# 2. Why we use excel file ?
'''Microsoft Excel enables users to format, organize and calculate data in a spreadsheet. 
By organizing data using software like Excel, 
data analysts and other users can make information easier to view as data is added or changed. 
Excel contains a large number of boxes called cells that are ordered in rows and columns.'''

# 3. Difference between .xls and .xlsx file?
'''The main comparison between these two files is that XLS uses the standard binary format, 
while XLSX applies the updated version that is based on the format of XML. In addition, 
the size of XLSX files can be compressed and reduced when they are changed to XLS files.'''

# Task: Create files and import in spyder and print data.

import pandas as pd
# 1. Create a friend_names.xls file  (atleast 10 names, columns are FriendName,Quality)
df_friend_names=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\friend_names.xls")
print(df_friend_names)

# 2. Create a family_members.xls file  (atleast 10 names, columns are FamilyMemberName*Relation)
df_family_members=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\family_members.xls")
print(df_family_members)

# 3. Create a Vegfood_items.xlsx file  (atleast 10 names, columns are VegFoodName*Taste)
df_Vegfood_items=pd.read_excel(r"C:\\Users\Abdul\\Downloads\\assignment8.a\\Vegfood_items.xlsx")
print(df_Vegfood_items)


# 4. Create a NonVegfood_items.xlsx file  (atleast 10 names, columns are NonVegFoodName*Taste)
df_NonVegfood_items=pd.read_excel(r"C:\Users\Abdul\Downloads\assignment8.a\NonVegfood_items.xlsx")
print(df_NonVegfood_items)


# 5. Create a month_names.xlsx file (atleast 12 names, columns are MonthName*Season)
df_month_names=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\month_names.xlsx")
print(df_month_names)


# 6. Create a colours_names.xlsx file  (atleast 12 names, columns are colourName_in_English^colourName_in_Hindi^colourName_in_Telugu)
df_colours_names=pd.read_excel(r"C:\\Users\\Abdul\\Downloads\\assignment8.a\\colours_names.xlsx")
print(df_colours_names)


