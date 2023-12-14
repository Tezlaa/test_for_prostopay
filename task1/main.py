from core.hashmap import HashMap


if __name__ == '__main__':
    hashmap = HashMap()
    hashmap['hello_command'] = 'Hello world, my name is Bogdan'
    
    print(hashmap['hello_command'])
    