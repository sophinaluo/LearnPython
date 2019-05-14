#汽车类，储存有关汽车的make，model，year等信息，创建get_decripetive_name类，打印相关数据
#创建一条相关用例
class Car():
	"""一次模拟汽车的简单尝试"""
	def __init__(self, make ,model ,year):
		"""初始化描述汽车性的属性"""
		self.make = make
		self.model = model
		self.year = year
		#增加属性
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")


	#通过方法修改属性的值
	def update_odometer(self, mileage):
		#将里程表的度读数设置为指定的值
		#添加一条逻辑，禁止任何人里程数往回调
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odemeter.")

	#通过方法对属性的值进行递增
	#设置一个初始的里程表读数 23500 ，购买车后是增加100英里的里程
	def increment_odometer(self,miles):
		"""将里程表读数增加指定的量"""
		self.odometer_reading += miles

#定义一个名为battery的新类，没有继承任何类
class Battery():
	"""一次模拟电动汽车电瓶的简单尝试"""
	def __init__(self, battery_size=70):
		"""初始化电瓶的属性"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print("this car has a " + str(self.battery_size) + "-kWh battery.")

	def upgrate_battery(self):
		if self.battery_size != 85:
			self.battery_size == 85

	#再给battery类添加一个方法，根据电瓶容量报告汽车的续航里程	
	def get_range(self):
		"""打印一条消息，指出电瓶的续航里程"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "this car can go approximately " + str(range)
		message += "miles on a full charge."
		print(message)
		self.upgrate_battery()

    
	

#9.3继承部分新增代码:如果重写了__init__ 时，实例化子类，就不会调用父类已经定义的 __init__
#创建一个简单的electriccar类版本，它具有car类的所有功能
#super()是一个特殊函数，帮助python 将父类和子类关联起来
class ElectricCar(Car):
		"""电动车的独特之处"""

		def __init__(self, make, model, year):
			"""初始化父类的属性
			初始化父类的属性，再初始化电动汽车特有的属性"""
			super().__init__(make, model, year)
#ElectricCar类必须有self.battery的属性,让python创建一个新的battery实例
#当_init_方法调用是，都将执行该操作，每个ElectricCar实例都包含一个自动创建的Battery实例
			self.battery = Battery()
			
		def describe_battery(self):
			self.battery_size.battery_size()

		def get_range(self):
			self.battery_size.get_range()
		


#重新父类的方法，只要不符合子类模拟的实物行为，都可以对此重写
#这种方法，只要重新的父类方法同名self
#如果有人对电动汽车调用方法fill_gas_tank(),程序将会忽略car类，转而执行这段
		def fill_gas_tank(self):
			"""电动汽车没有油箱"""
			print("This car doesn't  need a gas tank!")

#my_tesla的实例，代码先调用electriccar类的父类_init_()，再调用car类_init_()
my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
#创建一辆电动汽车，将其存储在变量my_tesla/中，使用属性battery，通过查找属性battery，对该事例使用方法describe_battery()
my_tesla.battery.describe_battery()
#my_tesla使用battery属性，并调用get_range方法
my_tesla.battery.get_range()
my_tesla.battery.get_range()








"""#9.2修改属性的代码

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())


#直接修改属性的值   

my_new_car.odometer_reading = 23

#通过方法修改的属性
my_new_car.update_odometer(23500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()
"""



		