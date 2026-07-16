# How We Solve UTF-8 Validation

Decode leading byte patterns and verify continuation bytes.

## Steps

1. From each leading byte, determine how many continuation bytes follow.
2. Require each continuation byte to start with the 10 prefix.
3. Reject malformed leads or leftover unfinished sequences.
