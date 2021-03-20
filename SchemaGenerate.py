import sys, ColorStr

def construct(data):
	print(ColorStr.parse(f"§YCREATE TABLE §0{data['class']}("))
	for i in data["primary"]:
		print(f"    {i},")
	for i in data["attrs"]:
		print(ColorStr.parse(f"    {i} §YNOT NULL§0,"))
	print(ColorStr.parse(f"    §YPRIMARY KEY§0 ({', '.join(data['primary'])})"))
	print(");")

data = {
	"class":"",
	"attrs":[],
	"primary":[]
} 
raw = ""
while 1:
	history = raw
	raw = input(">>")
	if raw.split(" "):
		if raw.split(" ")[0].lower() == "class":
			if len(raw.split(" ")) != 1:
				data["class"] = raw.split()[1]
		elif raw.split(" ")[0].lower() == "pri":
			if len(raw.split(" ")) != 1:
				data["primary"].append(raw.split()[1])
		elif raw.split(" ")[0].lower() == "go":
			print(data)
			construct(data)
			data = {
				"class":"",
				"attrs":[],
				"primary":[]
			}
		elif raw.split(" ")[0].lower() == "clear":
			data = {
				"class":"",
				"attrs":[],
				"primary":[]
			}
		elif raw.split(" ")[0].lower() == "undo":
			if history.split(" ")[0].lower() == "pri":
				data["primary"].remove(history.split(" ")[1])
			elif history.split(" ")[0].lower() == "class":
				data["class"] = ""
			else:
				data["attrs"].remove(history)
		elif raw.split(" ")[0].lower() == "exit":
			sys.exit(0)
		else:
			data["attrs"].append(raw)