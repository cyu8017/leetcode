# Approach
Join relations on shared followers for user pairs with `user1_id < user2_id`, then keep pairs achieving the max common-follower count.

# Complexity
Time depends on join size. Space O(pairs).
