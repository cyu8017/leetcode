# How We Solve Validate IP Address

Validate IPv4 and IPv6 formats separately; return Neither if both fail.

## Steps

1. IPv4: four dot-separated parts, each 0–255 without leading zeros (except `0`).
2. IPv6: eight colon-separated hex groups, each 1–4 hex digits.
3. Return the matching label or Neither.
