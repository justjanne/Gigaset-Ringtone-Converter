import sys

if __name__ == "__main__":
    for source in sys.argv[1:]:
        target = source.rsplit(".", 1)[0] + ".g722"
        print(f"Converting {source} to {target}")
        with open(source, "rb") as file:
            magic = file.read(4).decode("ascii")
            length = int.from_bytes(file.read(4), "little")
            name_length = int.from_bytes(file.read(1), "little")
            name = file.read(name_length).decode("ascii")
            checksum = file.read(16)
            payload_length = int.from_bytes(file.read(4), "little")
            with open(target, "wb") as output:
                for i in range(payload_length):
                    encrypted = file.read(1)[0]
                    decrypted = encrypted ^ (checksum[i % 16] + i) & 0xFF
                    output.write(bytes([decrypted]))
