#Counts number of times a function has been called
def count(fn):
    def wrapper(*args, **kwargs):
        wrapper.called += 1
        print(wrapper.called)
        return fn(*args, **kwargs)
    wrapper.called = 0
    wrapper.__name__ = fn.__name__
    return wrapper
