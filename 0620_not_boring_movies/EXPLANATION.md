# How We Solve Not Boring Movies

Filter odd ids that are not described as boring, then sort by rating.

## Steps

1. Keep rows where `id` is odd and `description != 'boring'`.
2. Order by `rating` descending.
