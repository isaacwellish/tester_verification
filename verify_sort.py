import sys

file1 = open(sys.argv[1],"r+")

print('opening: ', str(sys.argv[1]))

all_lines = file1.readlines()

# print all the lines first
for i in range(0, len(all_lines)):
    print(all_lines[i])
    #print(len(all_lines[i]))

wo_edit = []
wo_edit = [0 for i in range(len(all_lines))]

#unused for now, but would like to use to make code simpler
def erase_line():
    print('erase_line function')
    all_lines[i] = ''
    line = all_lines[i]

for i in range(0, len(all_lines)):
    line = all_lines[i]
    #print(len(all_lines[i]))
    if line == '':
        break
    else:
        line_first_char = line[0] # The first char of each line
        #print(line_first_char)
        # if first char is a ' ', check the next
       # if line_first_char == ' ':
        #    line_first_char = line[1]
         #   print('just a space, nothing to see here')
        # check if first char is a WO char
        # if first line doesn't start with a W and it doesn't start with a *
        # get rid of it! It's not a line we care about
        # mostly for lines like 'New Order:'
        #if line_first_char.isnumeric() == False:
        if (line_first_char != 'W') and (line_first_char != '*'):
            #erase_line()
            all_lines[i] = ''
            line = all_lines[i]
        # Check to see if the line is a short text based line (e.g *REV*)
        if len(all_lines[i])< 30:
            #erase_line()
            all_lines[i] = ''
            line = all_lines[i]

    wo = line.find('WO ')
    line_edit = line[(wo+3):(wo+7)]
    line_edit = line_edit.replace('-','')
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