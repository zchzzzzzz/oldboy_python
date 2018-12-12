# import shelve
# s1=shelve.open("2.txt")
# s1["name"]="zzz"
# s1["history"]={"age":11,"height":172}
# print(s1["history"]["age"])
# s1.close()
# import re
# print(re.search("abc|bcd","bcd"))
# print(re.search("a(bc)|(ef)g","bcef"))
# print(re.search("a(bc)|(ef)g","bcg"))
# print(re.search("a(bc)|(ef)g","efg"))
# str1="(12+(34*6+2-5*(2-1))"
# print(re.search("\([^(）]*\)",str1).group())
# x=re.search("\([^(）]*\)",str1).group().lstrip("(").rstrip(")")
# print(int(x)
# import re
# print(re.findall("(abc)+","abcabcccc"))
# print(re.findall("abc+","abcabcccc"))
# print(re.findall("(abc+)","abcabcccc"))
# print(re.findall("(?:abc)+","abcabcccc"))
import configparser
