# How We Solve Read N Characters Given Read4

Call read4 in a loop and copy characters into the destination until n are filled.

## Steps

1. Simulate read4 over the file string four characters at a time.
2. Copy as many as still needed into the destination buffer.
3. Stop early when read4 returns fewer than four characters.
4. Also stop once n characters have been copied.
5. Return the actual count written.
