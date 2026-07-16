# How We Solve Design Search Autocomplete System

Track sentence frequencies and, on each keystroke, return the top-3 matching prefixes.

## Steps

1. Initialize counts from historical sentences/times.
2. Append typed characters to the current buffer (except `#`).
3. On `#`, store the sentence; otherwise rank prefix matches by count then ASCII.
