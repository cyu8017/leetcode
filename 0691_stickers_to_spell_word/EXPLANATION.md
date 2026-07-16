# How We Solve Stickers to Spell Word

DP over the remaining letter-count state of `target`.

## Steps

1. Keep only sticker letters that appear in the target.
2. Memoize the minimum stickers needed for each remaining count tuple.
3. Always try stickers that cover the first still-needed letter; return `-1` if impossible.
