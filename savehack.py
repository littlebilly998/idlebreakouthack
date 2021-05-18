import base64

print("Idle Breakout Save Hack by Xsus")

print("What level do you want to be on?")
level = input(500000)

print("What amount of money would you like to have")
money = input(900000)

print("How much gold do you want")
gold = input(20000)

print("How many Black Boxes?")
bb = input(2100000000)

print("How many skillpoints")
sp = input(992929292992929)

s = f"{level},{money},{gold},2,0,0,0,0,0,0,0,1,1,0,43595.78,999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{bb},0,0,0,1,{sp},1,0,0"
b = s.encode("UTF-8")
e = base64.b64encode(b)
print("Encoding....")
print("Your result is....")
print(e)
print("\nCopy whats INSIDE the quotes\n")
end = 1
while end == 1:
    print("Once copied you may exit the console")
    input()
