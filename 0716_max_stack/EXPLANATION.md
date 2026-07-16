# How We Solve Max Stack

Stack plus a parallel max stack; `popMax` pops down to the max and restores.

## Steps

1. `push`/`pop`/`top` update both stacks together.
2. `peekMax` reads the max-stack top.
3. `popMax` buffers values above the max, removes it, then pushes the buffer back.
