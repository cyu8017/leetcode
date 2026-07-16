# How We Solve Sentence Screen Fitting

Simulate row filling word by word and count completed sentences.

## Steps

1. Pack words left to right with required spaces.
2. Wrap to the next row when the next word does not fit.
3. Increment the count whenever the word index wraps to zero.
