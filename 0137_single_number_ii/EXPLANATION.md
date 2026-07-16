# How We Solve Single Number II

Track bits seen once and twice so triples clear out.

## Steps

1. Maintain `ones` and `twos` bit masks.
2. For each number, update ones with bits not already in twos.
3. Update twos with bits not already in ones.
4. After three appearances, both masks clear that bit.
5. `ones` holds the unique number.
