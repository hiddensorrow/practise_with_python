# 生成200个激活码
# 2018年03月14日10:43:54
import random
import string

# upper_alphabet = [chr(ord('A') + i) for i in range(26)]
# lower_alphabet = [chr(ord('a') + i) for i in range(26)]
# candidate = upper_alphabet + lower_alphabet
candidate = string.ascii_letters
# print(upper_alphabet)
# print(lower_alphabet)
# print(candidate)
ans, times = dict(), 0
with open('res.txt', 'w') as f:
    while times < 200:
        res = ''
        for i in range(20):
          res += random.choice(candidate)
        if res not in ans:
            ans[res] = 1
            times += 1
            f.write(res+'\n')
# print(len(ans))
# for key, value in ans.items():
#     print(key)
