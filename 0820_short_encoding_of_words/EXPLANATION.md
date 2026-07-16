# How We Solve Short Encoding of Words

Only keep words that are not suffixes of another; encoding length is `sum(len+1)`.

## Steps

1. Put all words in a set.
2. Remove any proper suffix of another word.
3. Sum `length + 1` (`#`) over survivors.
