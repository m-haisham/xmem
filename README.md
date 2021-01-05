# Xmem

Simple to use, extensible key-based storage module.

Built around python dictionary.

## How to install

```bash
pip install xmem
```

## Example

You can use the templates as is

```python
from xmem import MemoryEngine

# for json based storage
from xmem.templates import JsonTemplate

# instantiate memory using save :path and :template instance
# path may be str, or pathlib.Path object
memory = MemoryEngine('data', JsonTemplate())

# optional: register save to python script exit event
memory.save_atexit()
```

or combine with different middleware for more specific use cases

```python
# raw template writes binary data
from xmem.templates import RawTemplate

# binary layer converts dict to bytes and vice versa
# encryption layer encrypts byte data and vice versa
from xmem.middleware import BinaryLayer, EncryptionLayer

# writes encrypted data to file
memory = MemoryEngine(
    'data',
    BinaryLayer(EncryptionLayer(RawTemplate(), key=[bytes]))
)

# optional: register save to python script exit event
memory.save_atexit()
```

### Combinations

- `BinaryLayer(RawTemplate())`
- `StringLayer(RegistryTemplate())`
- `BinaryLayer(RegistryTemplate())`
- `BinaryLayer(EncryptionLayer(RawTemplate(), key=[bytes])`
- `BinaryLayer(EncryptionLayer(RegistryTemplate(), key=[bytes])`

## [C](#create-update)[R](#read)[U](#create-update)[D](#delete)

### Create, Update

Create and update is handled using same functions.

`put`, `putall`

If key doesnt exist it would be created, else the value updated.

```python
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
```

### Read

```python
# read from memory using :get
two = memory.get('Two')

# output: 2
```

### Delete

```python
# delete keys using :delete
memory.delete('Two', 'Four')

# or clear the whole memory using :clear
memory.clear()
```

Method :delete takes one or more keys as parameters

## Create a template

A template has two methods that need to be overwridden

```python
def save(self, data: dict):
    ...
```

```python
def load(self) -> dict:
    ...
```
