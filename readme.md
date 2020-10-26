# readme


## 学生事务管理平台
    本项目使用基于python的django开发 djano version == 3.1.2 python version == 3.8.5 mysql version == 8.0.21


## 需求分析
---
    学生事务管理系统中应该存在三种角色: admin teacher student
    账号不允许自己创建，而应该由admin管理员创建，但是允许修改密码
    teacher账号功能:上传课程信息，管理选课人员，上传课程成绩。
    student账号功能:选课管理，查看课程成绩，课程评价
    admin账号功能:课程植入，账号管理