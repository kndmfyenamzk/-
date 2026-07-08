students = []
subjects = ['数学分析','高等代数','Python']
def add_student():
    print("\n=== 录入学生成绩 ===")
    name = input("请输入学生姓名")
    stu_id = input("请输入学生学号")
    for stu in subjects:
        if stu["学号"] == stu_id:
            print("该学号已存在，不能重复添加")
            return
    scores = {}
    for sub in subjects:
        while True:
            score_str = input(f"请输入{name}的{sub}成绩：")
            if score_str.replace(".","",1).isdigit():
                scores = float(score_str)
                if 0 <= scores < 100:
                        scores[sub] = scores
                        break
                else:
                        print("成绩应在0-100之间，请重新输入")
            else:
                    print("输入无效，请输入数字")
    student = {
         "姓名": name,
         "学号": stu_id,
         "成绩": scores
    }
    students.append(student)
    print(f"学生{name}的成绩录入成功")


def query_student():
    print("\n=== 查询学生成绩 ===")
    if len(students) == 0:
        print("还没有录入任何学生成绩")
        return
    choice = input("按学号查询请按1，按姓名查询请按2")
    if choice == '1':
        stu_id = input("请输入要查询的学号:")
        found = False
        for stu in students:
            if stu["学号"] == stu_id:
                print_student_info(stu)
                found = True
                break
        if not found:
            print("没有找到该学号的学生")
    elif choice == '2':
        name = input("请输入要查询的姓名")
        found = False
        for stu in students:
            if stu["姓名"] == name:
                print_student_info(stu)
                found = True
        if not found:
            print("没有找到该姓名的学生")
    else:
        print("请输入有效的数字")


def print_student_info(stu):
    print(f"\n姓名:{stu['姓名']}")
    print(f"学号：{stu['学号']}")
    print("各科成绩：")
    total = 0
    for sub, score in stu["成绩"].items():
        print(f"  {sub}:{score}")
        total += score
    avg = total / len(stu["成绩"])
    print(f"总分：{total}, 平均分：{avg:.2f}")


def show_statistics():
    print("\n=== 成绩统计 ===")
    if len(students) == 0:
        print("还没有录入任务学生成绩")
        return
    print(f"当前共有{len(students)}名学生")
    print("-"*30)
    subject_index = 0
    while subject_index < len(subjects):
        current_subject = subjects[subject_index]
        score_list = []
        student_index = 0
        while student_index < len(students):
            score_list.append(students[student_index]["成绩"][current_subject])
            student_index = student_index + 1
        total = 0
        i = 0
        while i < len(score_list):
            total = total + score_list[i]
            i = i + 1
        avg = total / len(score_list)

        highest = score_list[0]
        i = 0
        while i < len(score_list):
            if score_list[i] > highest:
                highest = score_list[i]
            i = i + 1

        lowest = score_list[0]
        i = 0
        while i < len(score_list):
            if score_list[i] < lowest:
                lowest = score_list[i]
            i = i + 1

        print(f"{current_subject}：平均分={avg:.2f}，最高分={highest}，最低分={lowest}")
        subject_index = subject_index + 1


def show_all_students():
    print("\n=== 所有学生成绩 ===")
    if len(students) == 0:
        print("还没有录入任何学生成绩")
        return
    print(f"共{len(students)}名学生")
    print("-"*50)
    for i, stu in enumerate(students):
        print(f"[{i+1}]姓名:{stu['姓名']},学号:{stu['学号']}")
        score_str = ".".join([f"{k}:{v}"for k,v in stu["成绩"].items()])
        print(f"    成绩:{score_str}")
    print("-"*50)


def main():
    print("="*40)
    print("     学生成绩管理系统")
    print("="*40)
    while True:
        print("\n请选择操作：")
        print("1,录入学生成绩")
        print("2,查询学生成绩")
        print("3,成绩统计分析")
        print("4,显示所有学生")
        print("0,退出系统")
        choice = input("请输入选项（0-4）：")
        if choice == '1':
            add_student()
        elif choice == '2':
            query_student()
        elif choice == '3':
            show_statistics()
        elif choice == '4':
            show_all_students()
        elif choice == '0':
            print("感谢使用，再见")
            break
        else:
            print("输入无效，请输入0-4之间的数字")
if __name__ == '__main__':
    main()