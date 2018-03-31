from decor import checkpoint1, checkpoint2, main_function

@checkpoint1
def my_cool_user_defined_func(global_object):
    print('\n\t\tUser: running my cool function')
    tom = global_object['potato']
    print(f'\t\tUser: I can access {tom}!\n')


@checkpoint2
def other_cool_func(global_object):
    print('\n\t\tUser: running my other cool function')
    global_object['potato'] = 'couch'
    print(f'\t\tUser: I can mutate global state too: {global_object["potato"]}\n')


@checkpoint2
def one_more_function(global_object):
    print('\n\t\tUser: This gets run right after the other_cool_function')
    global_object.update({'cool': 'shebang'})
    global_object.update({'my examples': 'are very corny'})
    print('\t\tUser: I shall update the global object with some cool shebang\n')


if __name__ == '__main__':
    main_function()
