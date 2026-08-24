# LeetCode 3903 - Smallest Stable Index I
# https://leetcode.com/problems/smallest-stable-index-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def first_stable_index(nums, k)
  n = nums.length
  right = Array.new(n, 0)
  right[n - 1] = nums[n - 1]
  (n - 2).downto(0) { |i| right[i] = [right[i + 1], nums[i]].min }
  left = 0
  n.times do |i|
    left = [left, nums[i]].max
    return i if left - right[i] <= k
  end
  -1
end
