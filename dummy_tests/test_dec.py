def dec(*args, **kwargs):
    def execute(func):
        print(f'Hello {kwargs.get("name")}')
        return func

    return execute


@dec(name='Brian')
def test_ex(surname='Pork'):
    print(surname)
    print('End')


if __name__ == '__main__':
    test_ex()
