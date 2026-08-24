# LeetCode 0910 - Smallest Range II
# https://leetcode.com/problems/smallest-range-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def smallest_range_ii(nums, k)
  nums.sort!
  ans = nums[-1] - nums[0]
  (0...(nums.length - 1)).each do |i|
    lo = [nums[0] + k, nums[i + 1] - k].min
    hi = [nums[-1] - k, nums[i] + k].max
    ans = [ans, hi - lo].min
  end
  ans
end
