# How We Solve Design Twitter

Store tweets by time and merge recent posts from followed users.

## Steps

1. Append each tweet with an increasing timestamp.
2. Collect the latest tweets from self and followees.
3. Return the ten most recent tweet ids.
