# LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

# @param {Integer[]} nums
# @return {Integer}
def reduction_operations(nums)
  nums = nums.sort
  answer = 0
  rank = 0

  (1...nums.length).each do |i|
    rank += 1 if nums[i] != nums[i - 1]
    answer += rank
  end

  answer
end
