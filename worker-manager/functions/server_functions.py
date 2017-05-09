import multiprocessing
from psutil import virtual_memory


# return numbers of cores
def get_number_of_cpu_cores():
    try:
        cpu_number = multiprocessing.cpu_count()
    except:
        print "error getting the number of cpu core"
        exit(2)
    return cpu_number


# return the amount of memory in mega the server has
def get_memory_size():
    try:
        mem = virtual_memory().total / 1000 / 1000
    except:
        print "error getting the number of cpu core"
        exit(2)
    return mem
