def raise_to_the_degrees (number):
    i=0
    while True:
        result=number**i
        yield result
        if result>100**20:
            return
        i+=1

res = raise_to_the_degrees(122345)
print(res)
for _ in res:
    print(_)

