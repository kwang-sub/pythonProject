ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is ", ab['Swaroop'])

del ab['Spammer']
print(len(ab))

for name, address in ab.items():
    print(name, " ", address)

ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print(ab['Guido'])