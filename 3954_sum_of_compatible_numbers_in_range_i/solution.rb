# LeetCode 3954 - Sum Of Compatible Numbers In Range I
# https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def sum_of_good_integers(n, k)
  start = [1, n - k].max
  finish = n + k
  ans = 0
  (start..finish).each { |x| ans += x if (n & x) == 0 }
  ans
end
