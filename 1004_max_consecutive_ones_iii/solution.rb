# LeetCode 1004 - Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def longest_ones(nums, k)
  left = zeros = ans = 0
  nums.each_with_index do |x, right|
    zeros += 1 if x.zero?
    while zeros > k
      zeros -= 1 if nums[left].zero?
      left += 1
    end
    ans = [ans, right - left + 1].max
  end
  ans
end
