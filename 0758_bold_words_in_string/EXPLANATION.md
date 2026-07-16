# How We Solve Bold Words in String

Mark every substring matching a word, then wrap contiguous marked runs.

## Steps

1. For each word, mark all occurrence ranges in `s`.
2. Scan left-to-right, wrapping maximal bold runs.
3. Emit the annotated string (`**…**` in local tests).
