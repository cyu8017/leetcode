# LeetCode 3064 - Guess the Number Using Bitwise Questions I
# https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

# The commonSetBits API is provided by the judge.

# @return {Integer}
def find_number
  n = 0
  32.times do |i|
    n |= 1 << i if common_set_bits(1 << i) > 0
  end
  n
end
