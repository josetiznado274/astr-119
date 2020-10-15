#define a dictionary data structure

#dictionaries have key : value for the lements
example_dict = {
	"class"			:	"Astr 119",
	"prof"			:	"Brant",
	"awseomeness"	:	10
}
print(type(example_dict))	#will say dict

#get a value via key
course = example_dict["class"]
print(course)

#change a value via ket
example_dict["awseomeness"] += 1	#increase awesomeness

#print the dictionary
print(example_dict)

#print dictionary element by elmement
for x in example_dict.keys():
	print(x,example_dict[x])