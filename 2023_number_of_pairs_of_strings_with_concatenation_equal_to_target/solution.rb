# LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

# @param {String[]} nums
# @param {String} target
# @return {Integer}
def num_of_pairs(nums, target)
  ans = 0
  nums.each_index do |i|
    nums.each_index do |j|
      ans += 1 if i != j && nums[i] + nums[j] == target
    end
  end
  ans
end
