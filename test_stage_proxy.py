def test_connection():
    from mr_box_peripheral_board.proxy_py3 import SerialProxy

    import time
    proxy = SerialProxy(port="COM5")
    time.sleep(2)
    # proxy = SerialProxy()
    assert proxy.ram_free() == 490
    exit(0)