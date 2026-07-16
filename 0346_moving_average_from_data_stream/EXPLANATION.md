# How We Solve Moving Average from Data Stream

A fixed-size queue maintains the running sum for O(1) averages.

## Steps

1. Append each new value and update total.
2. Drop the oldest value once size exceeds the window.
3. Return total divided by current window length.
