
# 9-3 用户 ： 创建一个名为User 的类， 其中包含属性first_name 和last_name ， 还有用户简介通常会存储的其他几个属性。 在类User 中定义一个名
# 为describe_user() 的方法， 它打印用户信息摘要； 再定义一个名为greet_user() 的方法， 它向用户发出个性化的问候。
# 创建多个表示不同用户的实例， 并对每个实例都调用上述两个方法


# 9-5 尝试登录次数 ： 在为完成练习9-3而编写的User 类中， 添加一个名为login_attempts 的属性。
# 编写一个名为increment_login_attempts() 的方法，它将属性login_attempts 的值加1。
# 再编写一个名为reset_login_attempts() 的方法， 它将属性login_attempts 的值重置为0。
# 根据User 类创建一个实例， 再调用方法increment_login_attempts() 多次。 打印属性login_attempts 的值，
# 确认它被正确地递增； 然后， 调用方法reset_login_attempts() ， 并再次打印属性login_attempts 的值， 确认它被重置为0。

class User():
	"""初始化用户表"""
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		"""打印用户名称方法"""
		print("用户名称是 ： " + self.first_name + self.last_name)
		# print('共登录用户量：' + str(self.login_attempts)) print('共登录用户量：(重置中……)'+str(self.login_attempts))
		print("共登陆用户量：" + str(self.login_attempts))


	def greet_user(self):
		print("你好～ " + self.first_name + self.last_name)

	def increment_login_attempts(self,number):
		self.login_attempts += number
		print("共登陆用户量： " + str(self.login_attempts))
	
	def reset_login_atttemps(self):
		self.login_attempts = 0

"""user_a = User('Ma','Yun')
user_a.increment_login_attempts(1)
user_a.increment_login_attempts(1)
user_a.increment_login_attempts(1)
user_a.reset_login_attempts()
user_a.describe_user()"""


# 9-7 管理员 ： 管理员是一种特殊的用户。 编写一个名为Admin 的类， 让它继承你为完成练习9-3或练习9-5而编写的User 类。
# 添加一个名为privileges 的属性， 用于存储一个由字符串（如"can add post" 、 "can delete post" 、 "can ban user" 等）
# 组成的列表。 编写一个名为show_privileges() 的方法， 它显示管理员的权限。 创建一个Admin 实例， 并调用这个方法。


class Admin(User):
	"""初始化admin类，继承user"""
	def __init__(self, first_name,last_name):
		super(Admin, self).__init__(first_name,last_name)
		#self.privileges = ('can add post','can delete post','can ban user')
		self.b = Privileges()


	def show_privileges(self):
		for i in self.privileges:
			print(i)


class Privileges():
	def __init__(self):
		self.privileges = ['can add post','can del post','can ban user']
		
	def show_privileges(self):
		for i in self.privileges:
			print("管理员权限有：" + i)
 
Admin1 = Admin('Ma','Yun')
Admin1.b.show_privileges()





		





"""		
user_a = User('Ma','Yun')
user_b = User('cheng','Long')
user_c = User('Li','LianJie')


user_a.describe_user()
user_a.greet_user()

user_b.describe_user()
user_b.greet_user()

user_c.describe_user()
user_c.greet_user()"""
