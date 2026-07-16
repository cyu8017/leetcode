# How We Solve Encode and Decode TinyURL

Short URLs must round-trip back to the original long URL.

## Steps

1. Keep bidirectional maps between long URLs and generated short codes.
2. Assign incrementing codes on first encode of a URL.
3. Decode by looking up the short URL in the reverse map.
