import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError
from database.repository import seed_teacher,seed_student, seed_grade, seed_group, seed_discipline,\
      remove_student, remove_teacher, remove_grade, remove_group, remove_discipline,\
      update_grade, update_group, update_teacher, update_student, update_discipline,\
      list_grade, list_group, list_teacher, list_student, list_discipline
      

parser = argparse.ArgumentParser(description='Todo APP')
parser.add_argument('--action', help='Command: create, update, list, remove')
parser.add_argument('--model')
parser.add_argument('--id_s')
parser.add_argument('--id_t')
parser.add_argument('--id_g')
parser.add_argument('--id_gr')
parser.add_argument('--id_d')
parser.add_argument('--name')
parser.add_argument('--grade')



arguments = parser.parse_args()
# print(arguments)
my_arg = vars(arguments)
# print(my_arg)

action = my_arg.get('action')
model = my_arg.get('model')
student_id = my_arg.get('id_s')
teacher_id = my_arg.get('id_t')
group_id = my_arg.get('id_g')
grade_id = my_arg.get('id_gr')
discipline_id = my_arg.get('id_d')
name = my_arg.get('name')
grade = my_arg.get('grade')

def check_data():
    print("Please, check the data you entered")

def main():
    match action:
        case 'create':
            if model == "Teacher":
                if name:
                    seed_teacher(name)
                else:
                    check_data()
            if model == "Student":
                if name and group_id:
                    seed_student(name, group_id)
                else:
                    check_data()
            if model == "Group":
                if name:
                    seed_group(name)
                else:
                    check_data()
            if model == "Grade":
                if grade and student_id and discipline_id:
                    seed_grade(grade, student_id, discipline_id)
                else:
                    check_data()
            if model == "Discipline":
                if name and teacher_id:
                    seed_discipline(name, teacher_id)
                else:
                    check_data()

        case 'remove':
            if model == "Discipline":
                if discipline_id:
                    r = remove_discipline(discipline_id)
                    print(f'Remove count: {r}')
                else:
                    check_data()
            if model == "Teacher":
                if teacher_id:
                    r = remove_teacher(teacher_id)
                    print(f'Remove count: {r}')
                else:
                    check_data()

            if model == "Student":
                if student_id:
                    r = remove_teacher(student_id)
                    print(f'Remove count: {r}')
                else:
                    check_data()
            if model == "Group":
                if group_id:
                    r = remove_teacher(student_id)
                    print(f'Remove count: {r}')
                else:
                    check_data()
            if model == "Grade":
                if grade_id:
                    r = remove_teacher(grade_id)
                    print(f'Remove count: {r}')
                else:
                    check_data()

        case 'update':
            if model == "Grade":
                if grade_id and student_id and discipline_id:
                    grade_upd = update_grade(grade_id, grade, student_id, discipline_id)
                    if grade_upd:
                        print("updated")
                    else:
                        print('Not found: 404')
            if model == "Teacher":
                if teacher_id:
                    teacher_upd = update_teacher(teacher_id, name)
                    if teacher_upd:
                        print("updated")
                    else:
                        print('Not found: 404')
            if model == "Group":
                if group_id:
                    group_upd = update_group(group_id, name)
                    if group_upd:
                        print("updated")
                    else:
                        print('Not found: 404')
            if model == "Student":
                if student_id and group_id:
                    student_upd = update_student(student_id, name, group_id)
                    if student_upd:
                        print("updated")
                    else:
                        print('Not found: 404')
            if model == "Discipline":
                if discipline_id and teacher_id:
                    discipline_upd = update_discipline(discipline_id, name, teacher_id)
                    if discipline_upd:
                        print("updated")
                    else:
                        print('Not found: 404')
        case 'list':
            if model == "Teacher":
                teachers = list_teacher()
                for t in teachers:
                    print(t.id, t.fullname)
            if model == "Student":
                students = list_student()
                for s in students:
                    print(s.id, s.fullname, s.group_id)
            if model == "Group":
                groups = list_group()
                for g in groups:
                    print(g.id, g.name)
            if model == "Discipline":
                disciplines = list_discipline()
                for d in disciplines:
                    print(d.id, d.name, d.teacher_id)
            if model == "Grade":
                grades = list_grade()
                for gr in grades:
                    print(gr.id, gr.grade, gr.student_id, gr.discipline_id)
            
         

if __name__ == '__main__':
    main()
