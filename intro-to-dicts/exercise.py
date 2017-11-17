hello = {
    'english': 'hello',
    'german': 'hallo',
    'polish': 'dzien dobry',
    'french': 'bonjour',
    'spanish': 'hola'
}

def print_dictionary():
    for k,v in hello.items():
        print(f'{k} - {v}')

def print_translation(word):
    print(hello[word])

print_dictionary()
print_translation('french')