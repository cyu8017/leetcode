# LeetCode 2553 - Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/

# @param {Integer[]} nums
# @return {Integer[]}
def separate_digits(nums)
  ans = []
  nums.each do |num|
    digits = []
    while num > 0
      digits << (num % 10)
      num /= 10
    end
    (digits.length - 1).downto(0) { |i| ans << digits[i] }
  end
  ans
end
