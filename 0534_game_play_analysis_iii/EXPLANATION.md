# How We Solve Game Play Analysis III

We need a running total of games played per player over time.

## Steps

1. Read rows from `Activity` ordered by player and date.
2. Use a window sum partitioned by `player_id`.
3. Return `player_id`, `event_date`, and the cumulative `games_played_so_far`.
