import logging


def log(func):

    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(f'{name}.log')
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
        logger.info(f'Running function {name}')
        result = func(*args, **kwargs)
        logger.info(f"Result: {result}")
        return func
    return wrap_log

        ##Qué significan los asteríscos colocados en los parámetros de la función?
        # def suma(*args):
        #     print(args)
        #     total = 0
        #     for number in args:
        #         total += number
        #     return total

        # print(suma(1,2,3,4,5))
        #Los asteríscos (*) indican que los parámetros a insertar serán
        #los indicados al momento de pasar los argumentos
        
        #(**kwargs) almacena llaves y argumentos en forma de diccionario



@log
def double_function(x):
    return x * 2
value = double_function(2)
print()

@log 
def suma(x, y):
    return x + y

suma  = suma(4,8)
