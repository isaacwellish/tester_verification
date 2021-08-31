import sys

file1 = open(sys.argv[1],"r+")

print('opening: ', str(sys.argv[1]))

all_lines = file1.readlines()
line1= all_lines[0]


for i in range(0, len(all_lines)):
    print(all_lines[i])

line1_edit = line1.replace('WO','')
line1_edit2 = line1[23:27]
wo = line1.find('WO ')
line1_edit3 = line1[(wo+3):(wo+7)]



wo_edit = []
wo_edit = [0 for i in range(len(all_lines))]

#delete the first line 
#all_lines[0] = ''

for i in range(0, len(all_lines)):

    line = all_lines[i]

    # check if first char is a number
    if line == '':
        break
    else:
        line_first_char = line[0]
        if line_first_char.isnumeric() == False:
            all_lines[i] = ''
            line = all_lines[i]

    wo = line.find('WO ')
    line_edit = line[(wo+3):(wo+7)]
    line_edit = line_edit.replace('-','')
    #line_edit = line_edit + '(' + i + ')' #add the order number 
    wo_edit[i] = line_edit

wo_edit = list(filter(None, wo_edit))

wo_edit_sorted = [int(numeric_string) for numeric_string in wo_edit]

wo_edit_sorted.sort()

wo_edit_sorted = [str(numeric_string) for numeric_string in wo_edit_sorted]



# Add the machines placement order to each line
for i in range(0, len(wo_edit)):
   for j in range(0, len(all_lines)):
        if wo_edit[i] == wo_edit_sorted[j]:
            wo_edit_sorted[j] = wo_edit_sorted[j] + '(' + str(i+1) + ')'
            break

# add verificaiton order to each line
print('sorted and ordered: ')
for i in range(0, len(wo_edit_sorted)):
    wo_edit_sorted[i] = str(i+1) + '. ' + wo_edit_sorted[i]
    print(wo_edit_sorted[i])

file1.close()


