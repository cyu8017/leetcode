# How We Solve Actors and Directors Who Cooperated At Least Three Times

Group by actor/director pair and keep pairs that appear at least three times.

## Steps

1. Group `ActorDirector` by `(actor_id, director_id)`.
2. Keep groups with `COUNT(*) >= 3`.
3. Return the matching pairs.
