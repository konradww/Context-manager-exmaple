class ContextManager:

    def __init__(self):
        pass

    def message(self, argument):
        print("Execute", argument )

    def __enter__(self):
        print("Start block with")
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
         if exception_type is None:
            print("normal exit")
            return True
         else:
            print("Save exception", exception_type)
            return False

with ContextManager() as context:
    context.message("test 1")
    print("OK - rightly")

print('{}'.format('-'*100))

with ContextManager() as context:
    context.message("test 2")
    raise TypeError
    print("NO - error")