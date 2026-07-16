# How We Solve Subdomain Visit Count

Parse each count/domain and add the count to every parent subdomain.

## Steps

1. Split `"count domain"` pairs.
2. For each suffix of the dotted domain, accumulate the count.
3. Format as `"count subdomain"` strings.
