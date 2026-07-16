# How We Solve Swap Adjacent in LR String

`XL→LX` moves L left; `RX→XR` moves R right; relative L/R order is fixed.

## Steps

1. After removing `X`, both strings must match.
2. Each `L` in start cannot be to the left of its counterpart in result.
3. Each `R` in start cannot be to the right of its counterpart in result.
