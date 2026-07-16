# How We Solve Tenth Line

Print only the tenth line of `file.txt`.

## Steps

1. Use `sed -n '10p'`.
2. Read `file.txt`.
3. Suppress all other lines.
4. Emit line 10 when it exists.
5. Produce empty output if the file is shorter.
