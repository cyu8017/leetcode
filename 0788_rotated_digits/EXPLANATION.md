# How We Solve Rotated Digits

A number is “good” if it only uses rotatable digits and changes under rotation.

## Steps

1. Valid digits: `0,1,2,5,6,8,9`; changing: `2,5,6,9`.
2. Count numbers in `1..n` whose digits are all valid and include a changer.
