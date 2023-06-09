# data type

name = "Pierre"
print(f"name = {name}, name isintanceof {type(name)} : {isinstance(name,str)}")
print("")
numb = 2023
print(f"numb = {numb}, numb isintanceof {type(numb)} : {isinstance(numb,int)}")
print("")
flot = 3.141
print(f"flot = {flot}, flot isintanceof {type(flot)} : {isinstance(flot,float)}")
print("")
ls = [3,4,7]
print(f"ls = {ls}, ls isintanceof {type(ls)} : {isinstance(ls,list)}")
print("")
dic = {"name": name, "numb": numb, "ls": ls}
print(f"dic = {dic}, dic isintanceof {type(dic)} : {isinstance(dic,dict)}")
print("")
tupl = (0,1,2,3,4,5,6)
print(f"tupl = {tupl}, tupl isintanceof {type(tupl)} : {isinstance(tupl,tuple)}")
print("")

# arithmetic operators

add = 1 + 1
sub = 2 - 1
mul = 2 * 2
div = 4 / 2
rem = 4 % 3
exp = 4 ** 2
fdv = 5 // 2

print(f" add : {add}, sub = {sub}, mul = {mul}, div = {div}, rem = {rem}, exp = {exp}, fdv = {fdv}")
print("")

# assignment operators

add += 1
sub -= 1
mul *= 2
div /= 2
rem %= 3
exp **= 2
fdv //= 2

print(f" add : {add}, sub = {sub}, mul = {mul}, div = {div}, rem = {rem}, exp = {exp}, fdv = {fdv}")
print("")

# comparaison operators

val1 = 10
val2 = 5
print(f"val1 = {val1}, val2 = {val2}")
print("")
equal_cmp = val1 == val2
print(f"equality operator '==' : val1 == val2 : {equal_cmp}")
print("")

not_equal_cmp = val1 != val2
print(f"not equal operator '!=' : val1 != val2 : {not_equal_cmp}")
print("")

superior = val1 > val2
print(f"superior operator '>' : val1 > val2 : {superior}")
print("")

inferior = val1 < val2
print(f"inferior operator '<' : val1 < val2 : {inferior}")
print("")

superior_or_equal = val1 >= val2
print(f"superior_or_equal operator '>=' : val1 >= val2 : {superior_or_equal}")
print("")

inferior_or_equal = val1 <= val2
print(f"inferior_or_equal operator '<=' : val1 <= val2 : {inferior_or_equal}")
print("")

# boolean or, not, is, and

print("or print the first non zero element")
print(f"0 or 0 = {0 or 0}")
print(f"0 or 1 = {0 or 1}")
print(f"1 or 0 = {1 or 0}")
print(f"1 or 1 = {1 or 1}")
print("")

print("and evaluates the second argument if and only if the first argument is true")
print(f"0 and 0 = {0 and 0}")
print(f"0 and 1 = {0 and 1}")
print(f"1 and 0 = {1 and 0}")
print(f"1 and 1 = {1 and 1}")
print("")

# bitwise operator

print(f"val1 = {val1}, val2 = {val2}")
print("")

print("bitwise '&' performs binary AND")
print(f"0 & 0 = {0 & 0}")
print(f"0 & 1 = {0 & 1}")
print(f"1 & 0 = {1 & 0}")
print(f"1 & 1 = {1 & 1}")
print(f"val1 & val2 = {val1 & val2}")
print("")

print("bitwise '|' performs binary OR")
print(f"0 | 0 = {0 | 0}")
print(f"0 | 1 = {0 | 1}")
print(f"1 | 0 = {1 | 0}")
print(f"1 | 1 = {1 | 1}")
print(f"val1 | val2 = {val1 | val2}")
print("")

print("bitwise '^' performs binary XOR")
print(f"0 ^ 0 = {0 ^ 0}")
print(f"0 ^ 1 = {0 ^ 1}")
print(f"1 ^ 0 = {1 ^ 0}")
print(f"1 ^ 1 = {1 ^ 1}")
print(f"val1 ^ val2 = {val1 ^ val2}")
print("")

print("bitwise '~' performs binary NOT")
print(f"~0 = {~0}")
print(f"~1 = {~1}")
print(f"~val1 = {~val1}")
print("")

print("bitwise '<<' shift left operation")
print(f"2 << 1 = {2 << 1}")
print("bitwise '>>' shift right operation'")
print(f"2 >> 1 = {2 >> 1}")
print("")

# identity operator

print(f"'is' is the identity operator, return true if an object is of the type of the compared object eg. name is name = {name is name}")
print("")
# membership operator

print(f"'in' is the membership operator, return true if an object or element is inside a collection eg. 3 in tupl= {3 in tupl}")
print("")

# ternary operator

print(f"In a function :\n\ndef is_adult(age):\n\tif age > 18:\n\t\treturn True\n\telse:\n\t\treturn False\n\nCan be simplified with ternary operator :\n\ndef is_adult(age):\n\treturn True if age > 18 else False\n")
print("")

# Strings

print("Strings can be written with single or double quotes, they are immutable and cannot be changed using indexes assginement like str = 'name'\nstr[3] = 'b' # this is illegal")
print("")
print("Instead to change the third letter in str one should assign to str a modified value as a whole :\n\nstr = str[:-1]+'b'")
string = "name"
print(f"str = {string}")
string = string[0:-1] + 'b'
print(f"str = {string}")
