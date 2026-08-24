# LeetCode 0634 - Find the Derangement of An Array
# https://leetcode.com/problems/find-the-derangement-of-an-array/

# @param {Integer} n
# @return {Integer}
def find_derangement(n)
  mod = 10**9 + 7
  return 0 if n == 1

  prev2 = 0
  prev1 = 1
  (3..n).each do |size|
    prev2, prev1 = prev1, (size - 1) * (prev1 + prev2) % mod
  end
  n > 1 ? prev1 : 0
end
