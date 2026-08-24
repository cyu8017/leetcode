# LeetCode 2824 - Count Pairs Whose Sum is Less than Target
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def count_pairs(nums, target)
  ans = 0
  (0...nums.length).each do |i|
    ((i + 1)...nums.length).each { |j| ans += 1 if nums[i] + nums[j] < target }
  end
  ans
end
