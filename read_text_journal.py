fn = "data/1995_2020.txt"


with open(fn, encoding="utf8") as f:
    lines = f.readlines()

print(len(lines))

years = range(1990, 2021)

for lno, line in enumerate(lines):
    for yr in years:
        if str(yr) in line:
            print(f"{yr} in {lno}: {line}")
