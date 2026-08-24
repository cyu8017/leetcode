# LeetCode 2104 - Sum of Subarray Ranges
# https://leetcode.com/problems/sum-of-subarray-ranges/

# @param {Integer[]} nums
# @return {Integer}
def sub_array_ranges(nums)
  n = nums.length
  ans = 0
  n.times do |i|
    mn = mx = nums[i]
    (i...n).each do |j|
      mn = [mn, nums[j]].min
      mx = [mx, nums[j]].max
      ans += mx - mn
    end
  end
  ans
end
