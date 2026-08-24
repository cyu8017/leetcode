# LeetCode 2012 - Sum of Beauty in the Array
# https://leetcode.com/problems/sum-of-beauty-in-the-array/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_beauties(nums)
  n = nums.length
  prefix_max = Array.new(n, 0)
  suffix_min = Array.new(n, 0)
  prefix_max[0] = nums[0]
  (1...n).each { |i| prefix_max[i] = [prefix_max[i - 1], nums[i]].max }
  suffix_min[n - 1] = nums[n - 1]
  (n - 2).downto(0) { |i| suffix_min[i] = [suffix_min[i + 1], nums[i]].min }
  ans = 0
  (1...n - 1).each do |i|
    if prefix_max[i - 1] < nums[i] && nums[i] < suffix_min[i + 1]
      ans += 2
    elsif nums[i - 1] < nums[i] && nums[i] < nums[i + 1]
      ans += 1
    end
  end
  ans
end
