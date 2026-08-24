# LeetCode 0674 - Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

# @param {Integer[]} nums
# @return {Integer}
def find_length_of_lcis(nums)
  best = 1
  cur = 1
  (1...nums.length).each do |i|
    if nums[i] > nums[i - 1]
      cur += 1
      best = [best, cur].max
    else
      cur = 1
    end
  end
  best
end
