 手机管理用户模块说明
 测试用户名：scholar
测试密码：scholar123456

用vue.js 和 api ，python结合 django ，在给出的静态页的基础上，实现网站手机端的「用户管理界面」，具有以下页面和功能：

1、页面1：一个展现网站所有用户的用户列表（列表中不包括超级管理员），对应 url 为 /m/userlistpanel/

功能1：用超级管理员身份登录后，点击按钮+NEW USER,可以添加2类用户：①网站新用户 普通身份 ②专栏作者

用超级管理员身份登录后，可以对用户进行管理，
①DELETE：可以删除列表上的用户
②Invited Author：可以赋予用户「专栏作者」身份的操作
③Ban this user：可以禁止该用户访问网站

2、页面2：访问用户列表所需的超级管理员登录页面，也就是登录超级管理员后才能访问用户列表，对应 url 为 /m/userlistpanel/login/

功能1：用户名以及密码的校验提示

功能2：非超级管理用户无法登录的身份限制功能

3、点击用户列表中的某个用户所进入的具体的「用户资料详情页」，对应 url 为 /m/userdetail/

可以修改该用户的用户名和密码

