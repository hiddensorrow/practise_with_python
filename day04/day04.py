# 将优惠券存至redis中
# 2018年03月15日16:03:00
import random
import string
import redis


red = redis.Redis(host='localhost', port=6379, db=1)
candidate = string.ascii_letters

ans, times = dict(), 0

p = red.pipeline()
while times < 200:
    res = ''
    for i in range(20):
      res += random.choice(candidate)
    if res not in ans:
        ans[res] = 1
        times += 1
        p.set(times, res)
p.execute()