title = input('Title: ')
author = input('Author: ')
journal = input('Journal: ')
volume = input('Volume: ')
pages = input('Pages: ')
year = input('Year: ')
keyword = input('Keyword: ')
filename = input('Path/Filename: ')
string = (
    '@article{' + keyword + ',\n' +
    'title={' + title + '},\n' +
    'author={' + author + '},\n' +
    'journal={' + journal + '},\n' +
    'volume={' + volume + '},\n' + 
    'pages={' + pages + '},\n' +
    'year={' + year + '},\n}\n'
)
with open(filename+'.bib', 'a+') as f:
    f.write(string)