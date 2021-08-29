file_1 =open("default_results.txt", "r")
file_2 =open("results.txt", "r")
content1 = file_1.read()
content2 = file_2.read()
list1 = content1.split("\n")
list2 = content2.split("\n")
counter1 = 0
counter2 = 0
for i in list1:
	if i:
		counter1 = counter1 + 1;
for j in list2:
	if j:
		counter2 = counter2 + 1;
print("default test cases:" + str(counter1) + "  result:" + str(counter2))

print("\n")
print("Files differ in " + str(sum(zipline[0]!=zipline[1] for zipline in zip(open('default_results.txt'), open('results.txt'))))+ " lines")

print("\n")
print("Percentage:" + str(100 - (sum(zipline[0]!=zipline[1] for zipline in zip(open('default_results.txt'), open('results.txt')))/counter1)*100))
