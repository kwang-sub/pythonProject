from getpass import _raw_input

try:
    text = _raw_input('Enter something --> ')
except EOFError:
    print("Why did you do an EOF on me?")
except KeyboardInterrupt:
    print("You cancelled the operation.")
else:
    print("You entered {}".format(text))