# LeetCode 2552 - Count Increasing Quadruplets
# https://leetcode.com/problems/count-increasing-quadruplets/

# @param {Integer[]} nums
# @return {Integer}
def count_quadruplets(nums)
  n = nums.length
  ans = 0
  great = Array.new(n, 0)
  n.times do |j|
    j.times do |i|
      if nums[i] < nums[j]
        ans += great[i]
      elsif nums[i] > nums[j]
        great[i] += 1
      end
    end
  end
  ans
end
