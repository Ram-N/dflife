import gspread

# gc = gspread.service_account()
gc = gspread.service_account(filename="df-life-f2050625a2e3.json")

sh = gc.open("_Yearly Grids")

worksheet = sh.worksheet("2011")

# worksheet_list = sh.worksheets()

# for ws in worksheet_list:
#    print(ws)


# for col in range(1, 10):
#     values_list = worksheet.col_values(col)
#     print(values_list)

# list_of_lists = worksheet.get_all_values()
list_of_dicts = worksheet.get_all_records()

for d in list_of_dicts:
    for k, v in d.items():
        print(k)
