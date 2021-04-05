### join
> "구분자".join(list)
- 구분자를 기준으로 list를 합쳐줌.

### list to string
``` python
s = "hello" 
s_list = list(s) #['h','e','l','l','o']
s_str = str(list) # ['h','e','l','l','o'] : list모양의 str임
s_str[0] #  [

str = "".join(s_list) # "hello"
str = "_".join(s_list) # "h_e_l_l_o"
```