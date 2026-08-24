# LeetCode 3255 - Find the Power of K-Size Subarrays II
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def results_array(nums, k)
  n = nums.length
  ans = Array.new(n - k + 1, 0)
  return nums.dup if k == 1
  streak = 1
  (1...n).each do |i|
    if nums[i] == nums[i - 1] + 1
      streak += 1
    else
      streak = 1
    end
    ans[i - k + 1] = streak >= k ? nums[i] : -1 if i >= k - 1
  end
  ans
end
