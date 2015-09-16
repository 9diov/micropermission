import inspect, functools
class PermissionDenied(Exception): pass

class Permission(object):
    def __init__(self, user = None):
        self.rules = []
        self.user = user

    def define_ability(self, action, klass, proc=None):
        self.rules.append((action, klass, proc))

    def can(self, action, obj):
        for rule in self.rules:
            action_rule, klass_object_rule, proc  = rule
            if inspect.isclass(klass_object_rule):
                if action == action_rule and \
                    (isinstance(obj, klass_object_rule) or obj is klass_object_rule) and \
                    (True if proc is None else proc(obj)):
                        return True
            else:
                if action == action_rule and obj == klass_object_rule:
                    return True

        return False

    def authorize(self, action, obj):
        def decorator(f):
            @functools.wraps(f)
            def wrapper(*args, **kwds):
                if not self.can(action, obj):
                    raise PermissionDenied
                else:
                    return f(*args, **kwds)
            return wrapper

        return decorator

class Note(object):
    def __init__(self, msg):
        self.message = msg

def can_define_class_rule():
    p = Permission()
    p.define_ability('read', Note)

    n = Note('message')
    assert p.can('read', n)

def can_define_object_rule():
    p = Permission()
    n = Note('message')
    p.define_ability('read', n)
    assert p.can('read', n)

def can_define_proc_rule():
    p = Permission()
    p.define_ability('read', Note, lambda n: n.message == 'hello')
    n = Note('message')
    assert not p.can('read', n)
    n = Note('hello')
    assert p.can('read', n)

def can_define_decorator():
    p = Permission()
    p.define_ability('read', Note)

    @p.authorize('read', Note)
    def read_note(n):
        pass

    n = Note('hello')
    read_note(n)

