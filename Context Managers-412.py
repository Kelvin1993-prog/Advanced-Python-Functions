## 2. Using Context Managers ##

with open('my_file.txt') as my_file:
    print(my_file.read())

## 3. Using Context Managers Continued ##

with open('alice.txt') as file:
    text = file.read()
    

n = 0
for word in text.split():
    if word.lower() in ['cat', 'cats']:
        n += 1

print('Lewis Caroll uses the word "cat" {} times'.format(n))



## 4. Writing Context Managers ##

import contextlib
import time
@contextlib.contextmanager
def timer():
    """Time the execution of a context block.

    Yields:
      None
    """
    yield
    start = time.time()
    # Send control back to the context block

    end = time.time()
    print('Elapsed: {:.2f}s'.format(end - start))

with timer():
    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)

## 5. Writing Context Managers Continued ##

import contextlib
@contextlib.contextmanager

def open_read_only(filename):
    """open a file in read-only mode.
    Args:
        filename(str): The location of the file to read
    
    Yields:
        file object
    """
    read_only_file = open(filename, mode='r')
    # Yield read_only_file so it can be assigned to my_file
    yield read_only_file
    read_only_file.close()
with open_read_only('my_file.txt') as my_file:
    print(my_file.read())

## 6. Nested Contexts ##

with stock('NVDA') as nvda:
    with open('NVDA.txt', 'w') as f_out:
        for _ in range(10):
            value = nvda.price()
            print('Logging ${:.2f}\n for NVDA'.format(value))
            f_out.write('{:.2f}\n'.format(value))

## 8. When to Create Context Managers ##

answer = 2