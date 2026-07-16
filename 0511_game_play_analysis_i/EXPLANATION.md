# How We Solve Game Play Analysis I

Aggregate each player's earliest login date with SQL.

## Steps

1. Group the `Activity` table by `player_id`.
2. Take `MIN(event_date)` as `first_login`.
3. Return one row per player.
