# How We Solve Remove Comments

Scan source with a block-comment flag; strip `//` and `/* */`.

## Steps

1. Outside a block, `//` ends the line and `/*` enters block mode.
2. Inside a block, skip until `*/`.
3. Flush non-empty line buffers when not in a block.
