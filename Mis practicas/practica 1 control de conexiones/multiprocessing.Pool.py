from multiprocessing import Pool

MAX_COUNT = 100000000
NUM_PROCESSES = 4


def count(max_count: int) -> int:
    counter = 0
    for _ in range(max_count):
        counter += 1
    print("Finished")
    return counter


if __name__ == "__main__":
    results = Pool(NUM_PROCESSES).map(count, [MAX_COUNT] * 5)
    print(results)