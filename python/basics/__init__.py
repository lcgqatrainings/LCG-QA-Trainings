filter_and_square = lambda lst:list(filter(lambda i: i is not None,[i*i if(i*i)>10 else None for i in lst]))
result = filter_and_square([2, 12, 9, 20])
print(result)

