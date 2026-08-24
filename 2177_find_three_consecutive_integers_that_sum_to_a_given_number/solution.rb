# LeetCode 2177 - Find Three Consecutive Integers That Sum to a Given Number
# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

# @param {Integer} num
# @return {Integer[]}
def sum_of_three(num)
  return [] if num % 3 != 0

  x = num / 3
  [x - 1, x, x + 1]
end
