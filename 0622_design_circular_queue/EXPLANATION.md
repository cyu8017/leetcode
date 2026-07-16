# How We Solve Design Circular Queue

Store elements in a fixed array with a head index and a size counter.

## Steps

1. `enQueue` writes at `(head + size) % capacity` when not full.
2. `deQueue` advances `head` when not empty.
3. `Front`/`Rear` read from the head and tail positions.
