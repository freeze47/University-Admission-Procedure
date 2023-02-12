# University-Admission-Procedure
It takes a lot of hard work to enroll in the university of your dreams. Although, we tend to dismiss how difficult it is for the university to handle the document volume. In this project, you'll deal with university applicants. We implement an algorithm to determine which applicants are going to be enrolled
# Introduction
This program is used to organize and process the information of applicants for admission to a university. The information for each applicant is contained in a text file, "applicants.txt", which includes their first name, last name, scores from exams in physics, chemistry, mathematics, computer science, and a special exam, as well as their preferred departments of study (up to three). The program processes this information and creates separate text files, one for each department, containing the names and scores of the accepted applicants.

## Input Data
The "applicants.txt" file contains one line for each applicant, with the following information:

``` python
<first name> <last name> <physics exam score> <chemistry exam score> <math exam score> <computer science exam score> <special exam score><department 1> <department 2> <department 3>
```
## Processing Information
The program processes the information from the "applicants.txt" file in the following way:

The user inputs the number of accepted students for each department.
The program reads each line of the "applicants.txt" file and stores the information for each applicant in a list, listOfApplicants.
The program calculates a score for each applicant for each of their preferred departments. The score is determined by taking the average of their exam scores in the relevant subjects, or the maximum of this average and their special exam score.
The program ranks the applicants in each department based on their scores, and selects the top numbOfAcceptedStudents applicants for each department, where numbOfAcceptedStudents is the number of accepted students entered by the user.
The program writes the names and scores of the accepted applicants for each department to separate text files, one for each department. The file names are in the format <department name>.txt.
## Output Files
The program creates one text file for each department, containing the names and scores of the accepted applicants. The file names are in the format <department name>.txt.
 
  The ranking of applicants for each department is calculated as follows:

Physics department: mean of scores for physics and math exams
Chemistry department: score for chemistry exam
Mathematics department: score for math exam
Engineering department: mean of scores for computer science and math exams
Biotech department: mean of scores for chemistry and physics exams
For each applicant, the highest score among the mean scores for final exams or the special exam's score will be chosen as the final score. If an applicant is not accepted in their first choice department, their final score will be re-calculated and compared with the requirements of their second choice department, and so on until they are either accepted into a department or all departments have been considered.
  
# Conclusion
This program provides a simple and efficient way to process the information of applicants for admission to a university and determine which applicants are accepted for each department based on their exam scores and preferred departments.
