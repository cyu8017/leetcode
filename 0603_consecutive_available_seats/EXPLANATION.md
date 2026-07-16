# How We Solve Consecutive Available Seats

A free seat is consecutive if an adjacent seat is also free.

## Steps

1. Self-join `Cinema` on neighboring `seat_id` values.
2. Keep seats where both sides of the join are free.
3. Return distinct seat ids in ascending order.
