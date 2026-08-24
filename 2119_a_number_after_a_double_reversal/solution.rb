# LeetCode 2119 - A Number After a Double Reversal
# https://leetcode.com/problems/a-number-after-a-double-reversal/

# @param {Integer} num
# @return {Boolean}
def is_same_after_reversals(num)
  num == 0 || num % 10 != 0
end
