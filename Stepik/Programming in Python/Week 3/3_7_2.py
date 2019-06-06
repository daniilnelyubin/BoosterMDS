string_in = input()
cipher_in = input()
string_on_encription = input()
string_on_decription = input()

dic_e = {}
dic_d = {}

for i in range(len(string_in)):
    dic_e[string_in[i]] = cipher_in[i]
    dic_d[cipher_in[i]] = string_in[i]
    
first_str = ""
second_str = ""

for i in string_on_encription:
    first_str+=dic_e[i]
for j in string_on_decription:
    second_str+=dic_d[j]
print(first_str)
print(second_str)
    





