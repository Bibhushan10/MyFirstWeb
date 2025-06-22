def convert (s):
    h=s//3600
    r=s%3600
    m=r//60
    sec=r%60
    return h,m,sec
s=int(input('Enter seconds'))
r1,r2,r3=convert(s)
print (f'Hours = {r1}')
print (f'Minutes = {r2}')
print (f'Seconds = {r3}')
