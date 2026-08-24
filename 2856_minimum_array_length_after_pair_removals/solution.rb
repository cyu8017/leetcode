# LeetCode 2856 - Minimum Array Length After Pair Removals
# https://leetcode.com/problems/minimum-array-length-after-pair-removals/

# @param {Integer[]} nums
# @return {Integer}
def min_length_after_removals(nums)
  n = nums.length
  freq = {}
  mx = 0
  nums.each do |v|
    c = freq.fetch(v, 0) + 1
    freq[v] = c
    mx = c if c > mx
  end
  return n % 2 if mx <= n / 2

  2 * mx - n
end
