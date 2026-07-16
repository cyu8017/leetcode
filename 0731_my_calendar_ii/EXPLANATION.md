# How We Solve My Calendar II

Track all bookings and their double-booked overlaps; reject triple overlap.

## Steps

1. If the new event hits any existing overlap interval, reject it.
2. Otherwise record new pairwise overlaps with prior bookings.
3. Append the event to the booking list.
