# 9-1 餐馆 ： 创建一个名为Restaurant 的类， 其方法__init__() 设置两个属性： restaurant_name 和cuisine_type 。 创建一个名
# 为describe_restaurant() 的方法和一个名为open_restaurant() 的方法， 其中前者打印前述两项信息， 而后者打印一条消息， 指出餐馆正在营业。


# 9-4 就餐人数 ： 在为完成练习9-1而编写的程序中， 添加一个名为number_served 的属性， 并将其默认值设置为0。
# 根据这个类创建一个名为restaurant 的实例； 打印有多少人在这家餐馆就餐过， 然后修改这个值并再次打印它。
# 添加一个名为set_number_served() 的方法， 它让你能够设置就餐人数。 调用这个方法并向它传递一个值， 然后再次打印这个值。
# 添加一个名为increment_number_served() 的方法， 它让你能够将就餐人数递增。 调用这个方法并向它传递一个这样的值：
# 你认为这家餐馆每天可能接待的就餐人数。
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)


	def open_restaurant(self):
		print("\nRestaurant is opening.")

	def number_served_info(self):
		print(self.restaurant_name + "，这家餐馆每天可能接待的就餐人数:  " + str(self.number_served))
		print("来" + self.restaurant_name + "吃" + self.cuisine_type + "的人有： " + str(self.number_served) + "人.")

	def set_number_served(self,number_info):
		self.number_served = number_info

	def increment_number_served(self,name_add):
		self.number_served += name_add


# 9-6 冰淇淋小店 ： 冰淇淋小店是一种特殊的餐馆。 编写一个名为IceCreamStand 的类， 让它继承你为完成练习9-1或练习9-4
# 而编写的Restaurant 类。 这两个版本的Restaurant 类都可以， 挑选你更喜欢的那个即可。 添加一个名为flavors 的属性，
# 用于存储一个由各种口味的冰淇淋组成的列表。 编写一个显示这些冰淇淋的方法。 创建一个IceCreamStand 实例， 并调用这个方法。
class  IceCreamstand(Restaurant):
	"""docstring for  IceCreamstand"""
	def __init__(self, restaurant_name,cuisine_type):
		super( IceCreamstand, self).__init__(restaurant_name,cuisine_type)
		self.flavors = ['apple','banana']

	def show_ice(self):
		for i in self.flavors:
			print(i)


IceCreamstand1 = IceCreamstand('北京菜','上海菜')
IceCreamstand1.show_ice()

"""
restaurant = Restaurant('紫光阁','北京菜')
restaurant.number_served = 30
restaurant.set_number_served(1)
restaurant.increment_number_served(100)
restaurant.increment_number_served(100)
restaurant.increment_number_served(100)
restaurant.increment_number_served(100)
restaurant.number_served_info()

#9-1		
#restaurant = Restaurant('chichi','chinese food')
#print(restaurant.restaurant_name, ' ',restaurant.cuisine_type)

#restaurant.describe_restaurant()
#restaurant.open_restaurant()

# 9-2 三家餐馆 ： 根据你为完成练习9-1而编写的类创建三个实例， 并对每个实例调用方法describe_restaurant() 。
restaurant1 = Restaurant('a','b')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('a2','b2')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('a3','b3')
restaurant3.describe_restaurant()"""
