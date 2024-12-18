from time import sleep as wait


class UdsServer:
    def __init__(self) -> None:
        print("message from my class init.")

    def process_dignostic_request(self, request: bytes) -> bytes:
        print("message from my class process_dignostic_request.")
        return b"response"
