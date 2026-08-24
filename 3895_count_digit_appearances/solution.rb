# LeetCode 3895 - Count Digit Appearances
# https://leetcode.com/problems/count-digit-appearances/

# @param {Integer[]} nums
# @param {Integer} digit
# @return {Integer}
def count_digit_occurrences(nums, digit)
  ans = 0
  nums.each do |num|
    x = num
    while x > 0
      ans += 1 if x % 10 == digit
      x /= 10
    end
  end
  ans
end
