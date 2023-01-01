from Designer.General import start,stop

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

# two attr
start("red","fg")
print("hello everyone")
stop()
# two attr
start("green",'bg',4)
print("it's print green background text with underline")
stop()
# single attr
start("blue")
print(a)
stop()

