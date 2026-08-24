# LeetCode 3178 - Find the Child Who Has the Ball After K Seconds
# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def number_of_child(n, k)
  mod = k % (n - 1)
  k = k / (n - 1)
  return n - mod - 1 if k.odd?
  mod
end
