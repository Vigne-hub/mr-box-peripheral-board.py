def test_connection():
    from mr_box_peripheral_board.proxy import SerialProxy

    import time
    proxy = SerialProxy()
    time.sleep(2)
    # proxy = SerialProxy()
    assert proxy.ram_free() == 490
    exit(0)

if __name__ == '__main__':
    from mr_box_peripheral_board.proxy import SerialProxy

    import time
    proxy = SerialProxy()
    time.sleep(2)
    # proxy = SerialProxy()
    if proxy.ram_free() == 490:
        print("SUCCESS, TEST PASSED")