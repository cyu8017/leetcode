# LeetCode 3094 - Guess the Number Using Bitwise Questions II
# https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

# The commonBits API is provided by the judge.

# @return {Integer}
def find_number
  n = 0
  32.times do |i|
    count1 = common_bits(1 << i)
    count2 = common_bits(1 << i)
    n |= 1 << i if count1 > count2
  end
  n
end
