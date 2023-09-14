# write a python program that takes in student name,class and thier section
#it should take 5marks ofthe student total marks and percentange mark

student_name = (input("student_name"))
class_of_student =(input ("class of student"))
semester = (input ("semester"))


#input 5 subject marks of student 
# we write float to cast the total str to float
programing_marks=float(input("programming_marks"))
htlm_marks=float(input("htlm_marks"))
data_sceince_marks=float(input("data_sceince_marks"))
computer_marks=float(input("computer_marks"))
graphics_marks=float(input("graphics_marks"))
#whatever comes from 


#totalmarks
total_marks=(programing_marks+htlm_marks+data_sceince_marks+computer_marks+graphics_marks)
print(total_marks)

#percentage marks
#every subject carries 100marks
# incase your given marks out of 60
#percentage mark= (average/60)*100
percentange_marks=(total_marks)/5
print(percentange_marks)

print("student name:", student_name)
print ("class:",class_of_student)
print("semester:",semester )



