# LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
# https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def minimum_sum(n, k)
  used = {}
  total = 0
  x = 1
  while used.length < n
    unless used[k - x]
      used[x] = true
      total += x
    end
    x += 1
  end
  total
end
