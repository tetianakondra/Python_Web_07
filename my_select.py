from sqlalchemy import func, desc, select, and_

from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    SELECT s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
    FROM grades g
    LEFT JOIN students s ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY avg_grade DESC
    LIMIT 5;
    :return:
    """
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
             .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2():
    """
    SELECT d.name, s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
    FROM grades g
    LEFT JOIN students s ON s.id = g.student_id
    LEFT JOIN disciplines d ON d.id = g.discipline_id
    WHERE d.id = 5
    GROUP BY s.id
    ORDER BY avg_grade DESC
    LIMIT 1;
    :return:
    """
    result = session.query(
                        Discipline.name,
                        Student.fullname,
                        func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                    .select_from(Grade).join(Student).join(Discipline)\
                    .filter(Discipline.id == 5)\
                    .group_by(Student.id, Discipline.name).order_by(desc('avg_grade')).limit(1).first()
    return result


def select_3():
    """
    SELECT gr.name, d.name, ROUND(AVG(g.grade), 2) as avarage_grade
    FROM grades g
    LEFT JOIN students s ON s.id = g.student_id
    LEFT JOIN disciplines d ON d.id = g.discipline_id
    LEFT JOIN [groups] gr ON gr.id = s.group_id 
    WHERE d.id = 1
    GROUP BY gr.id 
    ORDER BY AVG(g.grade) DESC;
    Знайти середній бал у групах з певного предмета.
    """
    result = session.query(
                        Group.name,
                        Discipline.name,
                        func.round(func.avg(Grade.grade), 2).label('avarage_grade'))\
                    .select_from(Grade).join(Student).join(Discipline).join(Group)\
                    .filter(Discipline.id == 1)\
                    .group_by(Group.id, Discipline.name).order_by(desc('avarage_grade')).all()
    return result


def select_4():
    """
    SELECT ROUND(AVG(g.grade), 2) as avarage_grade
    FROM grades g;
    Знайти середній бал на потоці (по всій таблиці оцінок).
    """
    result = session.query(
                        func.round(func.avg(Grade.grade), 2).label('avarage_grade'))\
                    .select_from(Grade).all()
    return result


def select_5():
    """
    SELECT t.fullname as teacher, d.name as discipline
    FROM disciplines d 
    LEFT JOIN teachers t ON t.id = d.teacher_id
    WHERE t.id = 5;
    Знайти які курси читає певний викладач.
    """
    result = session.query(
                        Teacher.fullname,
                        Discipline.name.label('discipline'))\
                    .select_from(Discipline).join(Teacher)\
                    .filter(Teacher.id == 2)\
                    .all()
    return result

def select_6():
    """
    SELECT gr.name as group_name, s.fullname as student
    FROM students s 
    LEFT JOIN groups gr ON gr.id = s.group_id
    WHERE gr.id = 3
    ORDER BY s.fullname;
    Знайти список студентів у певній групі.
    """
    result = session.query(
                        Group.name.label('Group'),
                        Student.fullname.label('Student'))\
                    .select_from(Student).join(Group)\
                    .filter(Group.id == 3)\
                    .order_by(Student.fullname).all()
    return result

def select_7():
    """
    SELECT gr.name as group_name, d.name as discipline, s.fullname as student, g.grade, g.date_of 
    FROM grades g 
    LEFT JOIN students s ON s.id = g.student_id
    LEFT JOIN disciplines d ON d.id = g.discipline_id 
    LEFT JOIN groups gr ON gr.id = s.group_id
    WHERE gr.id = 3 AND d.id = 2
    ORDER BY s.fullname DESC;
    Знайти оцінки студентів у окремій групі з певного предмета.
    """
    result = session.query(
                        Group.name.label('Group'),
                        Discipline.name.label('Discipline'),
                        Student.fullname.label('Student'),
                        Grade.grade, Grade.date_of)\
                    .select_from(Grade).join(Student).join(Discipline).join(Group)\
                    .filter(and_(Group.id == 1, Discipline.id == 1))\
                    .order_by(Student.fullname).all()
    return result


def select_8():
    """
    SELECT t.fullname as teacher, d.name as discipline, ROUND(AVG(g.grade), 2) as avarage_grade
    FROM grades g 
    LEFT JOIN disciplines d ON d.id = g.discipline_id 
    LEFT JOIN teachers t ON t.id = d.teacher_id
    WHERE t.id = 1
    GROUP BY d.name;
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    """
    result = session.query(
                        Teacher.fullname.label('Teacher'),
                        Discipline.name.label('Discipline'),
                        func.round(func.avg(Grade.grade), 2).label('avarage_grade'))\
                    .select_from(Grade).join(Discipline).join(Teacher)\
                    .filter(Teacher.id == 2)\
                    .group_by(Teacher.id, Discipline.name).all()
    return result


def select_9():
    """
    SELECT s.fullname as student, d.name as discipline
    FROM grades g 
    LEFT JOIN disciplines d ON d.id = g.discipline_id 
    LEFT JOIN students s ON s.id = g.student_id
    WHERE s.id = 4
    GROUP BY d.name;
    Знайти список курсів, які відвідує певний студент.
    """
    result = session.query(
                        Student.fullname.label('Student'),
                        Discipline.name.label('Discipline'))\
                    .select_from(Grade).join(Discipline).join(Student)\
                    .filter(Student.id == 2)\
                    .group_by(Student.id, Discipline.name).all()
    return result


def select_10():
    """
    SELECT d.name as discipline, s.fullname as student, t.fullname as teacher
    FROM grades g 
    LEFT JOIN disciplines d ON d.id = g.discipline_id 
    LEFT JOIN students s ON s.id = g.student_id
    LEFT JOIN teachers t ON t.id = d.teacher_id 
    WHERE s.id = 4 and t.id = 5
    GROUP BY d.name;
    Список курсів, які певному студенту читає певний викладач.
    """
    result = session.query(
                        Discipline.name.label('discipline'),
                        Teacher.fullname.label('Teacher'),
                        Student.fullname.label('Student'))\
                    .select_from(Grade).join(Discipline).join(Student).join(Teacher)\
                    .filter(and_(Student.id == 4, Teacher.id == 2))\
                    .group_by(Student.id, Teacher.id, Discipline.name).all()
    return result


def select_11():
    """
    SELECT s.fullname as student, t.fullname as teacher, ROUND(AVG(g.grade), 2) as avarage_grade
    FROM grades g 
    LEFT JOIN disciplines d ON d.id = g.discipline_id 
    LEFT JOIN students s ON s.id = g.student_id
    LEFT JOIN teachers t ON t.id = d.teacher_id 
    WHERE s.id = 2 and t.id = 3;
    Середній бал, який певний викладач ставить певному студентові.
    """
    result = session.query(
                        Student.fullname.label('Student'),
                        Teacher.fullname.label('Teacher'),
                        func.round(func.avg(Grade.grade), 2).label('avarage_grade'))\
                    .select_from(Grade).join(Discipline).join(Student).join(Teacher)\
                    .filter(and_(Student.id == 4, Teacher.id == 2))\
                    .group_by(Student.id, Teacher.id, Discipline.name).all()
    return result


def select_12_1():
    """
    SELECT gr.name as group_name, d.name as discipline, s.fullname as student, g.grade, g.date_of as last_lesson_date
    FROM grades g 
    LEFT JOIN disciplines d ON d.id = g.discipline_id 
    LEFT JOIN students s ON s.id = g.student_id
    LEFT JOIN groups gr ON gr.id = s.group_id 
    LEFT JOIN teachers t ON t.id = d.teacher_id 
    WHERE gr.id = 3 and d.id = 2 AND g.date_of = (
    SELECT g.date_of
    FROM grades g 
    LEFT JOIN disciplines d ON d.id = g.discipline_id 
    LEFT JOIN students s ON s.id = g.student_id
    LEFT JOIN groups gr ON gr.id = s.group_id 
    LEFT JOIN teachers t ON t.id = d.teacher_id 
    WHERE gr.id = 3 and d.id = 2
    GROUP BY s.id 
    ORDER BY g.date_of DESC
    LIMIT 1)
    GROUP BY s.id 
    ORDER BY g.date_of DESC;
    Оцінки студентів у певній групі з певного предмета на останньому занятті.
    """
    subquery = session.query(Grade.date_of)\
                            .select_from(Grade).join(Discipline).join(Student).join(Group).join(Teacher)\
                            .filter(and_(Group.id == 2, Discipline.id == 2))\
                            .group_by(Grade.date_of)\
                            .order_by(desc(Grade.date_of)).limit(1).first()
    
    result = session.query(
                        Group.name.label('Group'),
                        Discipline.name.label('Discipline'),
                        Student.fullname.label('Student'),
                        Grade.grade, Grade.date_of)\
                        .select_from(Grade).join(Discipline).join(Student).join(Group).join(Teacher)\
                        .filter(and_(Group.id == 2, Discipline.id == 2, Grade.date_of == subquery[0])).all()
    
    return result


def select_12_2():
    """
    -- Оцінки студентів у певній групі з певного предмета на останньому занятті.
    select s.id, s.fullname, g.grade, g.date_of
    from grades g
    join students s on s.id = g.student_id
    where g.discipline_id = 3 and s.group_id = 3 and g.date_of = (
        select max(date_of)
        from grades g2
        join students s2 on s2.id = g2.student_id
        where g2.discipline_id = 3 and s2.group_id = 3
    );
    :return:
    """
    subquery = (select(func.max(Grade.date_of)).join(Student).filter(and_(
                    Grade.discipline_id == 3, Student.group_id == 3
                )).scalar_subquery())

    result = session.query(Student.id, Student.fullname, Grade.grade, Grade.date_of)\
                    .select_from(Grade)\
                    .join(Student)\
                    .filter(and_(
                        Grade.discipline_id == 3, Student.group_id == 3, Grade.date_of == subquery
                    )).all()
    return result


if __name__ == '__main__':
    # print(select_1())
    # print(select_2())
    # print(select_3())
    # print(select_4())
    # print(select_5())
    # print(select_6())
    # print(select_7())
    # print(select_8())
    # print(select_9())
    # print(select_10())
    # print(select_11())
    print(select_12_1())
    # print(select_12_2())
