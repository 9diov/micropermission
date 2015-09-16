## Introduction

micropermission is a simple action-based permission library for Python. Permission rules are defined as ability to do some action against some resource.

## Example usage

    class Note(object):
        def __init__(self, msg):
            self.message = msg

    # Class based 
    p = Permission()
    p.define_ability('read', Note)
    n = Note('message')
    assert p.can('read', n)

    # Object based
    n = Note('message')

    p = Permission()
    p.define_ability('read', n)
    assert p.can('read', n)

    # Proc based
    p = Permission()
    p.define_ability('read', Note, lambda n: n.message == 'hello')
    n = Note('message')
    assert not p.can('read', n)
    n = Note('hello')
    assert p.can('read', n)

    # Decorator
    p = Permission()
    p.define_ability('read', Note)

    @p.authorize('write', Note)
    def read_note(n):
        pass

    n = Note('hello')
    read_note(n) # Raise PermissionDenied exception
