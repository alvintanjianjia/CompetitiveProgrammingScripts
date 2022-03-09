i=0
num_potential_customers = 0
like = []
dislike = []

pizza_dict = {}
with open('HashCode2022/Pizza/e_elaborate.in.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        if i == 0:
            num_potential_customers = int(line)
        elif i%2 == 1:
            like.append(line)
        else:
            dislike.append(line)

        i += 1

#print(num_potential_customers)
#print(like)
#print(dislike)

for element in like:
    element = element.split(' ')
    num_element = int(element[0])
    for i in range(1,int(num_element)+1):
        
        try:
            pizza_dict[element[i]] += 1
        except:
            pizza_dict[element[i]] = 1

for element in dislike:
    element = element.split(' ')
    num_element = int(element[0])
    for i in range(1,int(num_element)+1):
        
        try:
            pizza_dict[element[i]] -= 1
        except:
            pizza_dict[element[i]] = -1



#print(pizza_dict)
list_of_ingredients = []
for key,value in pizza_dict.items():
    if value > 0:
        list_of_ingredients.append(key)
list_of_ingredients_string = ''
for element in list_of_ingredients:
    list_of_ingredients_string = list_of_ingredients_string + element + ' '

f = open('HashCode2022/Pizza/e_ans.txt', 'w')
f.write(str(len(list_of_ingredients)) + ' ' + list_of_ingredients_string)
f.close()
print(str(len(list_of_ingredients)) + ' ' + list_of_ingredients_string)

