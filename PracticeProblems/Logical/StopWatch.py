"""
    A Stopwatch Program for measuring the time that elapses between
    the start and end clicks
                                                                    """

import time


def time_convert(time_elapsed):
    print("The time elapsed is {} seconds".format(time_elapsed))


def stopWatch():
    input("Press Enter to start")  # user input
    start_time = time.time()

    input("Press Enter to stop")  # user input
    end_time = time.time()

    time_elapsed = end_time - start_time  # computation
    time_convert(time_elapsed)


if __name__ == '__main__':
    stopWatch()
