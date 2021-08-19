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


all_lines[0] = ''

for i in range(0, len(all_lines)):

    #if the words STEMMA or stma are found IN THE BEGINNING of a line, make the line it's found in blank
    if (all_lines[i].find('STEMMA') == 2) or (all_lines[i].find('STEMMA')) == 3: #check to see if 'STEMMA' shows up within in the first line e.g. "==STEMMA== or == STEMMA =="
       all_lines[i] = ''
       print('STEMMA FOUND')
    elif all_lines[i].find('stma') != -1: #check to see if 'stma' shows up at all
        all_lines[i] = ''
        print('stma FOUND')

    line = all_lines[i]
    #print("this is line:" + line)
    wo = line.find('WO ')
    line_edit = line[(wo+3):(wo+7)]
    line_edit = line_edit.replace('-','')
    #line_edit = line_edit + '(' + i + ')' #add the order numner 
    wo_edit[i] = line_edit

wo_edit = list(filter(None, wo_edit))

wo_edit_sorted = [int(numeric_string) for numeric_string in wo_edit]

wo_edit_sorted.sort()

wo_edit_sorted = [str(numeric_string) for numeric_string in wo_edit_sorted]



for i in range(0, len(wo_edit)):
   for j in range(0, len(all_lines)):
        #print(wo_edit[i])
        #print(wo_edit_sorted[j])
        if wo_edit[i] == wo_edit_sorted[j]:
            wo_edit_sorted[j] = wo_edit_sorted[j] + '(' + str(i+1) + ')'
            #print("found: ", str(wo_edit_sorted[j]))
            break

##print('sorted and ordered: ', wo_edit_sorted)


print('sorted and ordered: ')
for i in range(0, len(wo_edit_sorted)):
    wo_edit_sorted[i] = str(i+1) + '. ' + wo_edit_sorted[i]
    print(wo_edit_sorted[i])

file1.close()


