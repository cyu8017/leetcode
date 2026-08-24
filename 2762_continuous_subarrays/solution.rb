# LeetCode 2762 - Continuous Subarrays
# https://leetcode.com/problems/continuous-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def continuous_subarrays(nums)
  ans = 0
  left = 0
  min_q = []
  max_q = []
  nums.each_with_index do |val, right|
    min_q.pop while !min_q.empty? && nums[min_q[-1]] > val
    max_q.pop while !max_q.empty? && nums[max_q[-1]] < val
    min_q << right
    max_q << right
    while nums[max_q[0]] - nums[min_q[0]] > 2
      left += 1
      min_q.shift if min_q[0] < left
      max_q.shift if max_q[0] < left
    end
    ans += right - left + 1
  end
  ans
end
