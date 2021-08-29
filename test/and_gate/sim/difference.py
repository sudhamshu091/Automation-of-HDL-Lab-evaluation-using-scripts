import difflib
  
with open('default_results.txt') as file_1:
    file_1_text = file_1.readlines()
  
with open('results.txt') as file_2:
    file_2_text = file_2.readlines()
  
# Find and print the diff:
print("\n")
for line in difflib.unified_diff(file_1_text, file_2_text, fromfile='default_results.txt', tofile='results.txt', lineterm=''):
    print(line)