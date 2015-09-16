from micropermission import Permission
import unittest

class Note(object):
    def __init__(self, msg):
        self.message = msg

class TestClass(unittest.TestCase):
    def setUp(self):
        pass

    def test_can_define_class_rule(self):
        p = Permission()
        p.define_ability('read', Note)

        n = Note('message')
        self.assertTrue(p.can('read', n))

    def test_can_define_object_rule(self):
        n = Note('message')

        p = Permission()
        p.define_ability('read', n)

        self.assertTrue(p.can('read', n))

    def test_can_define_proc_rule(self):
        p = Permission()
        p.define_ability('read', Note, lambda n: n.message == 'hello')
        n = Note('message')
        self.assertFalse(p.can('read', n))
        n = Note('hello')
        self.assertTrue(p.can('read', n))

unittest.main()
