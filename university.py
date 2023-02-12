import os

listOfApplicants = []
Biotech = []
Chemistry = []
Engineering = []
Mathematics = []
Physics = []
departments = [Biotech, Chemistry, Engineering, Mathematics, Physics]
references = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
referencesForfiles = ["biotech", "chemistry", "engineering", "mathematics", "physics"]

#os.chdir(r"Filepath")

def numberOfAcceptedStudents_():
    global numbOfAcceptedStudents
    numbOfAcceptedStudents = int(input("Enter number of accepted students: "))

def selectScore(x,y):
    if (x> y):
        return x
    else:
        return y



def listOfApplicants_():
    global listOfApplicants

    with open('applicants.txt', 'r') as file:
        for line in file:
            new_applicant = line.strip().split()
            name = new_applicant[0] + " " + new_applicant[1]
            department = [new_applicant[7], new_applicant[8], new_applicant[9]]
            score_prim = [float(new_applicant[2]),float(new_applicant[3]),float(new_applicant[4]),float(new_applicant[5])]
            score = []
            for dep in department:
                if (dep == "Biotech" ):
                    test = (score_prim[1] + score_prim[0]) / 2
                    score.append(selectScore(test,float(new_applicant[6])))
                elif (dep == "Physics"):
                    test = (score_prim[0] + score_prim[2]) / 2
                    score.append(selectScore(test, float(new_applicant[6])))
                elif (dep == "Mathematics"):
                    test = score_prim[2]
                    score.append(selectScore(test, float(new_applicant[6])))
                elif (dep == "Chemistry"):
                    test = score_prim[1]
                    score.append(selectScore(test, float(new_applicant[6])))
                else:
                    test =(score_prim[3] + score_prim[2]) / 2
                    score.append(selectScore(test, float(new_applicant[6])))


            listOfApplicants.append([name, department, score])





def rankings():
    global references, departments, Biotech, Chemistry, Engineering, Mathematics, Physics


    selectionList = [listOfApplicants,[],[],[]]

    for i in range (3):
        selectionList[i].sort(key=lambda x: (-x[2][i], x[0]))
        for app in selectionList[i]:
            index_ = references.index(app[1][0])
            if (len(departments[index_]) >= numbOfAcceptedStudents):
                updatedApplicant = app
                del updatedApplicant[1][0]
                selectionList[i+1].append(updatedApplicant)
            else:
                departments[index_].extend([[app[0],app[2][i]]])






    for dep in departments:
        dep.sort(key=lambda x: (-x[1], x[0]))
        dep[:] = dep[:numbOfAcceptedStudents]





def selection():
    for i in range(5):
        name_file = open('{0}.txt'.format(referencesForfiles[i]), 'w', encoding='utf-8')
        for j in range(len(departments[i])):
            name_file.write("{0} {1}\n".format(departments[i][j][0],departments[i][j][1]))

        name_file.close()


numberOfAcceptedStudents_()
listOfApplicants_()
rankings()
selection()






