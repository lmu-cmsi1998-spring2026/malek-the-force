from rle import rle
from rld import rld

def test(label, input):
    print(f'\n{label}')
    print(f'  input:    {input}')
    encoded = rle(input)
    print(f'  encoded:  {encoded}')
    decoded = rld(encoded)
    print(f'  decoded:  {decoded}')
    print(f'  match:    {decoded == input}')


test('all same characters',        'aaaaaaaaaa')
test('no runs',                    'abcdefghij')
test('mixed runs and singles',     'aaabbbcddddefa')
test('run at end',                 'abccccccccc')
test('run at start',               'aaaaaabcd')

def test_list(label, input):
    print(f'\n{label}')
    print(f'  input:    {input}')
    encoded = rle(input)
    print(f'  encoded:  {encoded}')
    decoded = rld(encoded, as_list=True)
    print(f'  decoded:  {decoded}')
    print(f'  match:    {decoded == input}')

test_list('list of symbols',       ['@','@','@','!','!','#','#','#','#','$'])
test_list('list no runs',          ['a','b','c','d','e','f','g'])
test_list('list mixed',            ['x','x','x','y','z','z','z','z','z','y'])
