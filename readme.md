# readme


## 学生事务管理平台
    本项目使用基于python的django开发 djano version == 3.1.2 python version == 3.8.5 mysql version == 8.0.21

---
## 需求分析

- 学生事务管理系统中应该存在三种角色: admin teacher student
- 账号不允许自己创建，而应该由admin管理员创建，但是允许修改密码
- teacher账号功能:上传课程信息，管理选课人员，上传课程成绩。
- student账号功能:选课管理，查看课程成绩，课程评价
- admin账号功能:课程植入，账号管理

- 学校中有若干个专业，每个专业每年招若干个班，每个班有若干个学生
- 课程分为必修课和选修课，必修课只能本专业的学生选择，比如数据库这门课程可以由计算机和软件工程专业的学生选择，但是别的专业的学生不能选择这门课。
- 一位教师可以给多个班代课，但是同一时间同一位教师只能带一门课
---
### 功能需求
1. 录入学生时应该录入包含学号，姓名，性别，出生年月，学院，专业，班级，课程，课程教师，成绩等信息
2. 按照学号，姓名，专业三种方式可以查询学生的基本信息
3. 学生可以在给出的课程列表中选择课程进行选修，但是本专业的必修课不能由其他专业的学生选择，同时，存在一些选修课是全校公选课，可以由所有学生选择
4. 课程存在课程容量，由老师设定，如果课程容量已满则学生不能选择该门课程
5. 学生可以查询自己已经选择的课程的成绩.
6. 课程信息包括课程名称，课程种类(选修，必修)，任课教师，上课时间，上课地点，课程容量，课程要求的前置课程
7. 录入课程的时候应该录入包括课程名称，课程种类(选修，必修)，上课时间，上课地点，课程容量，课程要求的前置课程，任课教师等信息
8. 老师的信息包括姓名，性别，出生年月，学院，专业，职称等.
9. 课程的信息由老师自行录入，录入后在学生选课完成后老师可以查看选择本门课程的学生的基本信息，并可以对学生的信息进行管理，如增加学生或者删除学生等
10. 课程的成绩由老师负责录入，成绩录入后老师则不可以对学生成绩进行修改.
11. admin管理员负责对老师和学生的信息进行管理，包括新学生信息的录入，按照学院-专业-班级的方式进行录入和管理。还有对老师信息进行管理，按照学院-专业的方式进行管理,同时admin应该可以对教师和学生的信息进行管理，如学生转专业或教师职称变化等.
12. 管理员属性包括账号，密码，所在学院等
---

### E-R图

![E-R图](.\E-R.png "E-R图")

--- 
### 数据表

#### 学生表
| name  | attr |
| ---  | --- |
| StuNum | charfield|
| StuName | charfield|
| StuAge | Intergerfield|
| StuSex | charfield|
| StuBirth | Datefield|
| StuCollege | charfield|
| StuPass | charfield|
| StuMajor | charfield|
| StuGra | Booleanfield|
#### 教师表
| name  | attr |
| ---  | --- |
| TeaNum | charfield|
| TeaName | charfield|
| TeaPass | charfield|
| TeaCollege | charfield|
| TeaMajor | charfield|
| TeaSex | charfield|
| TeaBirth | Datefield|
#### 管理员表
| name  | attr |
| ---  | --- |
| AdminUser | Intergerfield|
| AdminPass | charfield|
| AdminCollege | charfield|
#### 课程表
| name  | attr |
| ---  | --- |
| CourName | charfield|
| CourCredit | floatfield|
| CourPlace | charfield|
| CourType | charfield|
| CourReq | charfield|
| CourTea | charfield|
#### 成绩表
| name  | attr |
| ---  | --- |
| CouName | charfield|
| StuName | charfield|
| CourGrade | floatfield|
| TeaName | charfield| 

