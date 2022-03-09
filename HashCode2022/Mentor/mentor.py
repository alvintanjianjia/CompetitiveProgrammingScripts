num_contributors = 0
num_projects = 0
contributors = []
projects = []

contributors_skill = []
projects_requirement = []
current_skill_dict = {}

with open('HashCode2022/Mentor/b_better_start_small.in.txt') as f:
    line = f.readline()
    line = line.replace('\n', '')
    line = line.split(' ')
    #num_potential_customers = int(line)
    num_contributors = int(line[0])
    num_projects = int(line[1])

    for i in range (num_contributors):
        line = f.readline()
        line = line.replace('\n', '')
        line = line.split(' ')
        name = line[0]
        contributors.append(line[0])
        num_of_skills = int(line[1])
        temp_dict = {}
        for j in range(num_of_skills):
            line = f.readline()
            line = line.replace('\n', '')
            line = line.split(' ')
            temp_dict[line[0]] = int(line[1])
        temp_dict['name'] = name
        contributors_skill.append(temp_dict)
        

    for k in range(num_projects):
        line = f.readline()
        line = line.replace('\n', '')
        projects.append(line)
        line = line.split(' ')
        num_project_requirement = int(line[-1])
        temp_arr = []
        for l in range(num_project_requirement):
            line = f.readline()
            line = line.replace('\n', '')
            temp_arr.append(line)
        projects_requirement.append(temp_arr)

print('Contributors')
print(contributors)
print(contributors_skill)
print('Projects')
print(projects)
print(projects_requirement)

import random
def shuffle(array):
    array_duplicate = array.copy()
    random.shuffle(array_duplicate)
    return array_duplicate


current_total_score = 0
current_contributor = []
max_score = 100
current_day = 0
current_project = None
iteration = 0
while max_score >= current_total_score:
    print('Iteration', iteration)
    iteration += 1
    current_order = shuffle(projects)

    #print(current_order)
    
    current_index = []
    for element in current_order:
        #print(element)
        #print(projects.index(element))
        current_index.append(projects.index(element))

    #current_index = [1,0,2]
    #current_total_score = 34

    current_total_score = 0
    current_day = 0
    for element in current_index:

        project_required_days = int(projects[element].split(' ')[1])
        project_score = int(projects[element].split(' ')[2])
        project_deadline = int(projects[element].split(' ')[3])
        project_required_contributors = int(projects[element].split(' ')[4])

        current_requirement = projects_requirement[element]
        '''
        for requirement in current_requirement:
            requirement = requirement.split(' ')
            if current_skill_dict.get(requirement[0]) > int(requirement[1]):
                current_day += 1

        '''
        temp_contributor = contributors_skill.copy()
        num_contributors = 0
        project_temporary_contributor = []
        temp_current_contributor = []
        for requirement in current_requirement:
            requirement = requirement.split(' ')
            #print(requirement, 'requirement')
            
            for contributor in temp_contributor:
                #print(contributor,'contributor')
                if contributor.get(requirement[0]) is not None:
                    if contributor.get(requirement[0]) >= int(requirement[1]):
                        temp_current_contributor.append(contributor['name'])
                        project_temporary_contributor.append(contributor)
        
        for requirement in current_requirement:
            requirement = requirement.split(' ')
            #print(requirement, 'requirement')
            
            for contributor in temp_contributor:
                #print(contributor,'contributor')
                if contributor.get(requirement[0]) is not None:
                    if contributor in project_temporary_contributor:
                        if contributor.get(requirement[0]) >= int(requirement[1]):
                            contributor[requirement[0]] += 1
                        #current_contributor.append(contributor['name'])
                        #project_temporary_contributor.append(contributor)

        
                       
        #print(current_contributor, 'current contributor in loop')
        current_contributor.append(temp_current_contributor)
             
        
        '''
        for contributor in project_temporary_contributor:
            print(contributor, 'lololol')
            for requirement in current_requirement:
                requirement = requirement.split(' ')
                if contributor.get(requirement[0]) is not None:
                    if contributor.get(requirement[0]) < int(requirement[1]):
                        temp_contributor[]

        '''


        #if num_contributors < project_required_contributors:
            #break
        current_day += project_required_days


        overdue_days = current_day - project_deadline
        #print('overdue days',overdue_days)
        
        if overdue_days > 0:
            after_iteration_score = project_score - overdue_days
            current_total_score += after_iteration_score
        else:
            current_total_score += project_score
        print(current_total_score)
    #print('Current Index: ', current_index)
    #print('Current score for this index: ', current_total_score)
    #print('Contributor timetable', current_contributor)

    if max_score < current_total_score:
        max_score = current_total_score
        f = open('HashCode2022/Mentor/c_ans.txt', 'w')
        f.write(str(len(current_index)) + '\n')
        counter = 0
        for element in current_index:
            f.write(projects[element].split(' ')[0] + '\n')
            collaborators_str = ''
            current_workforce = current_contributor[counter]
            print(current_workforce)
            for string in current_workforce:
                string += ' '
                collaborators_str += string
            counter += 1
            f.write(collaborators_str + '\n')

        f.close()

    


