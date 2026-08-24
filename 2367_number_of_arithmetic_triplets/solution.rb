# LeetCode 2367 - Number of Arithmetic Triplets
# https://leetcode.com/problems/number-of-arithmetic-triplets/

# @param {Integer[]} nums
# @param {Integer} diff
# @return {Integer}
def arithmetic_triplets(nums, diff)
  seen = {}
  nums.each { |x| seen[x] = true }
  ans = 0
  nums.each { |x| ans += 1 if seen[x + diff] && seen[x + 2 * diff] }
  ans
end
