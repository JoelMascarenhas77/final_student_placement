train_set = [['Red','Sports','Domestic','Yes'],
             ['Red','Sports','Domestic','No'],
             ['Red','Sports','Domestic','Yes'],
             ['Yellow','Sports','Domestic','No'],
             ['Yellow','Sports','Imported','Yes'],
             ['Yellow','SUV','Imported','No'],
             ['Yellow','SUV','Imported','Yes'],
             ['Yellow','SUV','Domestic','No'],
             ['Red','SUV','Imported','No'],
             ['Red','Sports','Imported','Yes']]
total = 10
stolen_yes = 0
stolen_no = 0

for i in range(total):
    if train_set[i][3] == 'Yes':
        stolen_yes += 1
    else:
        stolen_no += 1

P_stolen_yes = stolen_yes/total
P_stolen_no = stolen_no/total

print("NAIVE BAYES")
color = input("Enter color: ")
type = input("Enter type: ")
origin = input("Enter origin: ")
x = [color, type, origin]
color_yes = 0
color_no = 0
type_yes = 0
type_no = 0
origin_yes = 0
origin_no = 0
for i in range(total):
    if train_set[i][0] == x[0] and train_set[i][3] == 'Yes':
        color_yes += 1
    if train_set[i][0] == x[0] and train_set[i][3] == 'No':
        color_no += 1
    if train_set[i][1] == x[1] and train_set[i][3] == 'Yes':
        type_yes += 1
    if train_set[i][1] == x[1] and train_set[i][3] == 'No':
        type_no += 1
    if train_set[i][2] == x[2] and train_set[i][3] == 'Yes':
        origin_yes += 1
    if train_set[i][2] == x[2] and train_set[i][3] == 'No':
        origin_no += 1

epsilon = 0.01

p_color_yes = (color_yes + epsilon) / (stolen_yes + 3 * epsilon)
p_color_no = (color_no + epsilon) / (stolen_no + 3 * epsilon)
p_type_yes = (type_yes + epsilon) / (stolen_yes + 3 * epsilon)
p_type_no = (type_no + epsilon) / (stolen_no + 3 * epsilon)
p_origin_yes = (origin_yes + epsilon) / (stolen_yes + 3 * epsilon)
p_origin_no = (origin_no + epsilon) / (stolen_no + 3 * epsilon)

p_yes_x = P_stolen_yes * p_color_yes * p_type_yes * p_origin_yes
p_no_x = P_stolen_no * p_color_no * p_type_no * p_origin_no

print("Probability of Yes given X = ", round(p_yes_x,3))
print("Probability of No given X = ", round(p_no_x,3))

if p_yes_x > p_no_x:
    print(round(p_yes_x,3), " > ", round(p_no_x,3))
    print("Stolen = Yes")
else:
    print(round(p_no_x,3), " > ", round(p_yes_x,3))
    print("Stolen = No")
