# How We Solve Similar RGB Color

Round each two-digit hex channel to the nearest shorthand `XX` (`0x11` steps).

## Steps

1. Parse each `RR`, `GG`, `BB` channel as an integer.
2. Round to the nearest multiple of 17 via `(x + 8) // 17`.
3. Emit `#` plus three repeated hex digits.
