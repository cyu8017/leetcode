# LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
# https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def count_distinct_strings(s, k)
  mod = 1_000_000_007
  n = s.length
  ans = 1
  (n - k + 1).times { ans = (ans * 2) % mod }
  ans
end
