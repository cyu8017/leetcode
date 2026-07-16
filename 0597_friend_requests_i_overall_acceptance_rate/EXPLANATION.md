# How We Solve Friend Requests I: Overall Acceptance Rate

Acceptance rate is distinct accepted pairs over distinct requested pairs.

## Steps

1. Count distinct `(requester_id, accepter_id)` pairs.
2. Count distinct `(sender_id, send_to_id)` pairs.
3. Divide, treat no-requests as 0, and round to two decimals.
