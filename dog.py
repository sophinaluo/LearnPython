#创建dog类，每个小狗蹲下，打滚等能力
class  Dog():
	def __init__(self,name,age):
		#初始化属性name和age
		self.name = name
		self.age = age

	def sit(self):
		#模拟小狗被命令时蹲下
		print(self.name.title() + "is now sitting.")

	def roll_over(self):
		#模拟小狗被命令时打滚
		print(self.name.title() + "is now rolled over.")

		
my_dog = Dog('willie','6')
your_dog = Dog('marry','5')

print("my dog name is " + my_dog.name.title())
print("my dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nyour dog name is " + your_dog.name.title())
print("your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
