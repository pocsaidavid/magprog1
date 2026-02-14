import multiprocessing
import time

def cpu_stresser():
    while True:
        _ = 100 * 100

if __name__ == "__main__":
    cores = multiprocessing.cpu_count()

    processes = []

    for _ in range(cores):
        p = multiprocessing.Process(target=cpu_stresser)
        p.start()
        processes.append(p)

    try:
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
