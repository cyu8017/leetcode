# How We Solve Random Pick with Blacklist

Map blacklisted values in `[0, M)` onto whitelist values in `[M, n)`, then sample `[0, M)`.

## Steps

1. Let `M = n - len(blacklist)`.
2. Remap each blacklist entry `< M` to a white number `>= M`.
3. `pick` draws an index in `[0, M)` and applies the remap if needed.
