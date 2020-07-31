from xmem import MemoryEngine

# for json based storage
from xmem.templates import JsonTemplate

# or for pickle based storage
from xmem.templates import PickleTemplate

# instantiate memory using save :path and :template instance
# path may be str, or pathlib.Path object
memory = MemoryEngine('data', JsonTemplate())

# optional: register save to python script exit event
memory.save_atexit()


# add or update memory using :put
# method :put may be chained
memory\
    .put('One', 1)\
    .put('Two', 2)

# or by using :putall
memory.putall({
    'three': 3,
    'Four': 4
})


# read from memory using :get
two = memory.get('Two')  # 2


# delete keys using :delete
memory.delete('Two', 'Four')

# or clear the whole memory using :clear
memory.clear()
