
# 6-5 河流 ： 创建一个字典， 在其中存储三条大河流及其流经的国家。 其中一个键—值对可能是'nile': 'egypt' 。
# 使用循环为每条河流打印一条消息， 如“The Nile runs through Egypt.”。
# 使用循环将该字典中每条河流的名字都打印出
rivers = {'huanghe':'China','changjiang':'China','nile':'Egypt'}
for k,v in rivers.items():
	print("the" + k + "runs through" + v + ".")
for k in rivers.items():
	print(k)
for v in rivers.items():
	print(v)
