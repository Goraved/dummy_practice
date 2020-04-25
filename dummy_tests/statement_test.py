print('--> First task:')
st = 'Print only the words that start with s in this sentence'
lst = [word for word in st.split() if word[0] == 's']
print(f'Answer = {lst}')

print('--> Second task:')
even_nums = [num for num in range(0, 11, 2)]
print(f'Answer = {even_nums}')

print('--> Third task:')
divisible_three_nums = [num for num in range(0, 50, 3)]
print(f'Answer = {divisible_three_nums}')

print('--> Fourth task:')
st_even = 'Print every word in this sentence that has an even number of letters'
lst_even = [f'"{word}" is even!' for word in st_even.split() if len(word) % 2 == 0]
print(f'Answer = {lst_even}')

print('--> Fifth task:')
fizz_list = []
for num in range(100):
    if num % 3 == 0 and num % 5 == 0:
        fizz_list.append('FizzBuzz')
    elif num % 3 == 0:
        fizz_list.append('Fizz')
    elif num % 5 == 0:
        fizz_list.append('Buzz')
    else:
        fizz_list.append(num)
print(f'Answer = {fizz_list}')

print('--> Sixth task:')
st_first = 'Create a list of the first letters of every word in this string'
first_lst = [letter[0] for letter in st_first.split()]
print(f'Answer = {first_lst}')