# How We Solve Game Play Analysis II

Join each player's first login row to get the device used that day.

## Steps

1. Subquery the minimum `event_date` per `player_id`.
2. Join back to `Activity` on player and that date.
3. Select `player_id` and `device_id`.
