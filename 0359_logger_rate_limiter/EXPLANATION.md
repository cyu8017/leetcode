# How We Solve Logger Rate Limiter

Remember the last printed timestamp for each message.

## Steps

1. On a new message, allow printing and store the timestamp.
2. On repeats within ten seconds, reject printing.
3. Allow printing again once ten seconds have elapsed.
