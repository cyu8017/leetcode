# LeetCode 1085 - Sum of Digits in the Minimum Number
# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_digits(nums)
  n = nums.min
  digit_sum = 0
  while n.positive?
    digit_sum += n % 10
    n /= 10
  end
  digit_sum.even? ? 1 : 0
end
