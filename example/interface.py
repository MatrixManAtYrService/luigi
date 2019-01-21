from luigi import define
from luigi import call
import json
import example.app as app

# define any custom types to be used for i/o
class Words:
    pass

# entrypoints:

def add():
    call.fromcli(app.add)
define.func(add, (int, int)) # register in/out types with luigi

def sub():
    call.fromcli(app.sub)
define.func(sub, (int, int))

def say():
    call.fromcli(app.say)
define.func(say, (int, Words))

def count():
    call.fromcli(app.count)
define.func(count, (Words, int))

def shout():
    call.fromcli(app.shout)
define.func(shout, (Words, Words))


def whisper():
    call.fromcli(app.whisper)
define.func(whisper, (Words, Words))

print(define.as_dot())


class Words(list):

    # __init__ should accept whatever is most convenient for use in the app
    # in this case it's a list of strings
    def __init__(self, arg):
        self = arg

    # from_str can be omitted if __init__ accepts a single string
    # otherwise, it should consume whatever to_str creates
    # in this case it's a json-serialized list of strings
    def from_pipe(in_str):
        return Words(json.loads(in_str))

    # if __init__ accepts a string, to_str should provide that string
    # if not, to_str should provide whatever from_str consumes
    def to_pipe():
        return json.dumps(self)

    # if the user will provide input compatible with from_pipe, this can be omitted
    # used to detect the type of user-provided input, in cases like:
    #    echo "five six" | add
    # returns an instance if this class is the handler, None otherwise
    # In this case, accepts strings like "foo bar baz" but rejects any strings containing numbers
    def from_user(in_str):
        if any(set(in_str).intersection(set(['0123456789']))):
            return None
        else:
            return Words(list(filter(any, in_str.split(' '))))

    # if the user can happily view the output of to_pipe, this can be omitted
    # returns a string fit for user consumption
    def to_user(self, in_str):
        return ' '.join(self)
