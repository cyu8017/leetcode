# LeetCode 0728 - Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/

# @param {Integer} left
# @param {Integer} right
# @return {Integer[]}
def self_dividing_numbers(left, right)
  is_self_dividing = lambda do |num|
    x = num
    while x > 0
      digit = x % 10
      return false if digit == 0 || num % digit != 0

      x /= 10
    end
    true
  end

  (left..right).select { |num| is_self_dividing.call(num) }
end
