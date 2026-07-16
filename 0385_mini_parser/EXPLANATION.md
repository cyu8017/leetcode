# How We Solve Mini Parser

Stack-based parsing builds nested lists as brackets open and close.

## Steps

1. If the string is a plain integer, return a NestedInteger wrapper.
2. Push a new list on '[' and attach completed integers on ',' or ']'.
3. Pop finished lists into their parent when ']' closes a segment.
