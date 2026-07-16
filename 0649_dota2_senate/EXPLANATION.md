# How We Solve Dota2 Senate

Simulate bans with two queues of senator indices.

## Steps

1. Queue Radiant and Dire positions separately.
2. The earlier senator bans the later one and rejoins at `index + n`.
3. The party with remaining senators wins.
