from datetime import datetime

from sqlalchemy import and_
from sqlalchemy.exc import SQLAlchemyError

from database.db import session
from database.models import Teacher, Student, Discipline, Grade, Group


def seed_teacher(fullname):
    teacher = Teacher(fullname=fullname)
    session.add(teacher)
    session.commit()
    session.close()


def seed_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    session.close()


def seed_student(fullname, group_id):
    group = session.query(Group).filter(Group.id == group_id).all()
    if group:
        student = Student(fullname=fullname, group_id=group_id)
        session.add(student)
        session.commit()
    else:
        print('there is no group with group_id = {group_id}')
    session.close()


def seed_discipline(name, teacher_id):
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).all()
    if teacher:
        discipline = Discipline(name=name, teacher_id=teacher_id)
        session.add(discipline)
        session.commit()
    else:
        print(f"there is no teacher with this id")
    session.close()


def seed_grade(grade, student_id, discipline_id):
    student = session.query(Student).filter(Student.id == student_id).all()
    discipline = session.query(Discipline).filter(Discipline.id == discipline_id).all()
    if student and discipline:
        date_of = datetime.now()
        grade = Grade(grade=grade, date_of=datetime.date(), student_id=student_id, discipline_id=discipline_id)
        session.add(grade)
        session.commit()
    else:
        print('there is no data with such ids')
    session.close()


def remove_student(id_s):
    result = session.query(Student).filter(Student.id == id_s).delete()
    session.commit()
    session.close()
    return result

def remove_grade(id_gr):
    result = session.query(Grade).filter(Grade.id == id_gr).delete()
    session.commit()
    session.close()
    return result

def remove_teacher(id_s):
    result = session.query(Teacher).filter(Teacher.id == id_t).delete()
    session.commit()
    session.close()
    return result

def remove_group(id_g):
    result = session.query(Group).filter(Group.id == id_g).delete()
    session.commit()
    session.close()
    return result

def remove_discipline(id_d):
    result = session.query(Discipline).filter(Discipline.id == id_d).delete()
    session.commit()
    session.close()
    return result


def update_student(id_s, name, id_g):
    student = session.query(Student).filter(Student.id == id_s)
    if student:
        student.update({"fullname": name, "group_id": id_g})
        session.commit()
        session.close()
        return student.first()
    return student


def update_discipline(id_d, name, id_t):
    discipline = session.query(Discipline).filter(Discipline.id == id_d)
    if discipline:
        discipline.update({"name": name, "teacher_id": id_t})
        session.commit()
        session.close()
        return discipline.first()
    return discipline


def update_teacher(id_t, name):
    teacher = session.query(Teacher).filter(Teacher.id == id_t)
    if teacher:
        teacher.update({"fullname": name})
        session.commit()
        session.close()
        return teacher.first()
    return teacher


def update_group(id_g, name):
    group = session.query(Group).filter(Group.id == id_g)
    if group:
        group.update({"name": name})
        session.commit()
        session.close()
        return group.first()
    return group

def update_grade(id_gr, grade, id_s, id_d):
    grade = session.query(Grade).filter(Grade.id == id_gr)
    if grade:
        grade.update({"grade": grade, "student_id": id_s, "discipline_id": id_d})
        session.commit()
        session.close()
        return grade.first()
    return grade


def list_grade():
    grades = session.query(Grade).all()
    session.close()
    return grades


def list_teacher():
    teachers = session.query(Teacher).all()
    session.close()
    return teachers


def list_group():
    groups = session.query(Group).all()
    session.close()
    return groups


def list_student():
    students = session.query(Student).all()
    session.close()
    return students


def list_discipline():
    disciplines = session.query(Discipline).all()
    session.close()
    return disciplines
    
    


















