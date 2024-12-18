from py_dummy_uds_server import UdsServer


def test_importing():
    cls_instance = UdsServer()
    assert cls_instance.process_dignostic_request(b'1001')
