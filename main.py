import time


def decorator(path):
    def _decorator(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            named_tuple = time.localtime()
            time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'Дата и время вызова: {time_string}\n')
                file.write(f'Имя: {old_function.__name__}\n')
                file.write(f'Аргументы: {args}, {kwargs}\n')
                file.write(f'Возвращаемое значение: {result}\n\n')
            return result
        return new_function
    return _decorator


@decorator('function_logs.txt')
def func():
    return 'Функция выполнена'


if __name__ == '__main__':
    func()
