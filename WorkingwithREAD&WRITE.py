# from pathlib import Path
# p = Path('testing.txt')
# p.write_text("This is our first writing text.")
# print(p.read_text())

import shelve
shelffile = shelve.open('myfile')
values = ['one','apple','cat']
shelffile['values'] = values
shelffile.close()

shelffile = shelve.open('myfile')
print(shelffile)
print(shelffile['values'])

