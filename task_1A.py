f_size  = int(input("Enter size of grid:"))

forest_map = []
for i in range(f_size):
    row = list(map(int, input().split()))
    forest_map.append(row)

print(f"Forest map: {forest_map}")

extraction_zone = []
m = int(input("Size of extraction zone:"))
r = int(input("Input row:"))
c = int(input("Input column:"))
if m%2!=0:
    for i in range(r-((m-1)//2), (r+((m-1)//2))+1):
        row = []
        for j in range(c-((m-1)//2), (c+((m-1)//2))+1):
            row.append(forest_map[i][j])
        
        extraction_zone.append(row)
else:
    for i in range(r-((m-1)//2), (r+((m-1)//2))+2):
        row = []
        for j in range(c-((m-1)//2), (c+((m-1)//2))+2):
            row.append(forest_map[i][j])
        
        extraction_zone.append(row)

print("Extaction Zone:")
print(extraction_zone)

count = 0
for i in range(len(extraction_zone[0])):
    for j in range(m):
        if extraction_zone[i][j] == 1:
            count += 1
print(f"Total Lal Chandan Trees in Zone: {count}")
