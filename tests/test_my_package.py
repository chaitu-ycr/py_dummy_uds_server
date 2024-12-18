from py_dummy_uds_server import MyClass


def test_importing():
    cls_instance = MyClass()
    assert cls_instance.say_hello()
