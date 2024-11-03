import datetime
emp={}#قاموس لتخزين جميع الموظفين
#دالة تقوم بأضافة و تعديل موظف
def add(mode):
    try:
        print("\t\t||\n\t\t||_____________________________________________")
        id=int(input("\t\t||\n\t\t||\n\t\t||----->   enter employee ID  :"))
    except:
        print("\t\t||\n\t\t||\n\t\t||             sory failde input\n\t\t||\n\t\t||_____________________________________________")
        return
    if (id not in emp and mode == "add") or ( mode == "update" and id in emp):
        name=input("\t\t||\n\t\t||\n\t\t||----->   enter employee name  :")
        try:
            salary=int(input("\t\t||\n\t\t||\n\t\t||----->   enter employee salary  :"))
        except:
            print("\t\t||\n\t\t||\n\t\t||    sory failde input a must be number\n\t\t||\n\t\t||_____________________________________________")
            return
        dep=input("\t\t||\n\t\t||\n\t\t||----->   enter employee department  :")
        try:
            date=datetime.date.today()
        except:
            print("\t\t||\n\t\t||\n\t\t||      somthing wooring try again\n\t\t||\n\t\t||_____________________________________________")
        if id not in emp and mode != "update":
           emp[id]={'id':id,'name':name,'salary':salary,'department':dep,'joing-date':date}
        elif mode == "update" and id in emp:
            emp[id]={'id':id,'name':name,'salary':salary,'department':dep,'joing-date':date}
        sortn()
    else:    
        print("\t\t||\n\t\t||\n\t\t||   sorry not exssist" if mode == "update" else "\t\t||\n\t\t||\n\t\t||   sorry id is exssist")
#دالة حذف موظف
def dele():
    try:
        id=int(input("\t\t||\n\t\t||\n\t\t||----->   enter employee ID :"))
    except:
        print("\t\t||\n\t\t||\n\t\t||          sory failde input must be number\n\t\t||\n\t\t||_____________________________________________")
        return
    if id in emp:
       del emp[id]
       print("\t\t||\n\t\t||\n\t\t||          deletede completed")
    else:
        print('\t\t||\n\t\t||\n\t\t||               not found')
    print("\t\t||\n\t\t||_____________________________________________")
#دالة لعرض تقرير للموظفين او الاطلاع على الموظفين  الموجدين
def viw_emp(mode):
    if emp !={}:
        for a in emp:
            for k ,s in emp[a].items():
                if mode =='all':
                    print(f"\t\t||----->   {k} : {s}")
                elif mode=="name":
                    print(f"\t\t||----->   employee[{emp[a]["id"]}]: {emp[a]["name"]}")
                    break
            print("---------------------------------")
    else:
        print("\t\t||\n\t\t||\n\t\t||       not found any employees")
    print("\t\t||\n\t\t||_____________________________________________")
#ID دالة للبحث عن موظف باتخدام 
def ser_id():
    try:
        id=int(input("\t\t||\n\t\t||\n\t\t||----->   enter employee ID :"))
    except:
        print("\t\t||\n\t\t||\n\t\t||  sory failde input must be number\n\t\t||\n\t\t||_____________________________________________")
        return
    if id in emp:
        for k ,s in emp[id].items():
           print(f"\t\t||----->   {k} : {s}")
    else:
        print("\t\t||\n\t\t||\n\t\t||          not found")
    print("\t\t||\n\t\t||_____________________________________________")
#name دالة للبحث عن موظف باتخدام 
def ser_name():
    name=input("\t\t||\n\t\t||\n\t\t||----->   enter employee name :")
    for a in emp:
        if emp[a]["name"]==name:
            for k ,s in emp[a].items():
                print(f"\t\t||----->   {k} : {s}")
            print("\t\t||\n\t\t||_____________________________________________")
            return
    print("\t\t||\n\t\t||\n\t\t||          not found")
    print("\t\t||\n\t\t||_____________________________________________")

#دالة لعرض الاقسام و مجموع الرواتب لكل قسم
def gr():
    dep={}
    for a in emp:
        if emp[a]["department"] in dep:
            dep[emp[a]["department"]] += emp[a]["salary"]
        else:
            dep[emp[a]["department"]] = emp[a]["salary"]
    for a in dep:
        print(f"\t\t||----->   {a} : {dep[a]}")
    print("\t\t||\n\t\t||_____________________________________________")
#ID دالة لترتيب الموظفين عبر 
def sortn():
    global emp
    emp = dict(sorted(emp.items()))
#دالة لجلب اعلى او ادنى راتب او تاريخ 
def min_max(mode):
    max_s= max(emp, key=lambda x: emp[x][mode])
    min_s= min(emp, key=lambda x: emp[x][mode])
    print(f"\t\t||\n\t\t||\n\t\t||----->   last injoin: {emp[max_s][mode]}"if mode=='joing-date'else f"\t\t||\n\t\t||\n\t\t||----->   max salary: {emp[max_s][mode]}")
    print(f"\t\t||----->   first join: {emp[min_s][mode]}"if mode=='joing-date'else f"\t\t||----->   min salary: {emp[min_s][mode]}")
    print("\t\t||\n\t\t||_____________________________________________")


while True==True:
    print("\t\t||           oprition name              ||  ID\n\t\t||______________________________________||_____\n\t\t||---->  add employee                   ||   1\n\t\t||---->  update employee                ||   2\n\t\t||---->  delete employee                ||   3")
    print("\t\t||---->  view all employees             ||   4\n\t\t||---->  search employee by ID          ||   5\n\t\t||---->  search employee by name        ||   6\n\t\t||---->  salary for eath department     ||   7\n\t\t||---->  viw max and mi salari          ||   8\n\t\t||---->  last injoin and ferst injoin   ||   9\n\t\t||---->          report                 ||   10")
    print("\t\t||---->           exei                  ||   11\n\t\t||______________________________________||_____")
    ch=input("\t\t||              ID:  ")
    ch=ch   
    if ch=='1':add("add")
    elif ch=='2':add("update")
    elif ch=='3':dele()
    elif ch=='4':viw_emp("name")
    elif ch=='5':ser_id()
    elif ch=='6':ser_name()
    elif ch=='7':gr()
    elif ch=='8':min_max("salary")
    elif ch=='9':min_max("joing-date")
    elif ch=='10':viw_emp("all")
    elif ch=='11':exit()