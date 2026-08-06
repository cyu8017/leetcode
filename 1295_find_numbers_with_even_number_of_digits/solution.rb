# LeetCode 1295 - Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

# @param {Integer[]} nums
# @return {Integer}
def find_numbers(nums)
  nums.count { |value| value.to_s.length.even? }
end
