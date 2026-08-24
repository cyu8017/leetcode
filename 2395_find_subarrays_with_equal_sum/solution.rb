# LeetCode 2395 - Find Subarrays With Equal Sum
# https://leetcode.com/problems/find-subarrays-with-equal-sum/

# @param {Integer[]} nums
# @return {Boolean}
def find_subarrays(nums)
  seen = {}
  (0...nums.length - 1).each do |i|
    s = nums[i] + nums[i + 1]
    return true if seen[s]
    seen[s] = true
  end
  false
end
