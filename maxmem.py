import time
import sys

def memory_stresser():
    data = []
    block_size_mb = 100

    try:
        while True:
            data.append(bytearray(

                1024 * 1024 * block_size_mb))

            total_allocated = len(data) * block_size_mb
            time.sleep(0.1)

    except MemoryError:
        print("\n[!] Betelt a memória")
    except KeyboardInterrupt:
        print("\nLeállítva. Memória felszabadítása...")


if __name__ == "__main__":
    memory_stresser()
