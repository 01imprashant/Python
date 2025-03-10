chai='Masala Chai'
print(chai)
print(chai[0])
print(chai[-1])
print(chai[0:6])

num_list='0123456789'
print(num_list)
print(num_list[:])
print(num_list[3:])
print(num_list[:7])
print(num_list[::2])
print(num_list[::3])

print(chai)
print(chai.lower())
print(chai.upper())

chai='  Masala Chai  '
print(chai)
print(chai.strip())

chai='Lemon Chai'
print(chai)
print(chai.replace('Lemon','Ginger'))
print(chai)

chai='lemon, ginger, mint, masala'
print(chai)
print(chai.split())
print(chai.split(', '))

chai='Masala chai'
print(chai.find('Chai'))

chai='Masala chai chai chai chai'
print(chai.count('chai'))

chai_type='Masala'
quantity=2
order='I ordered {} cups of {} chai'
print(order.format(quantity,chai_type))

chai_variety=['masala','ginger','lemon']
print(chai_variety)
print(''.join(chai_variety))
print(' '.join(chai_variety))
print(', '.join(chai_variety))
print('-'.join(chai_variety))

chai='Masala chai'
print(chai)
print(len(chai))

for letter in chai:
    print(letter)


# chai="He said,\n" masala chai is awasome"\

chai=r"c:\user\pwd"
print(chai)

chai='masala chai'
print('maasala' in chai)