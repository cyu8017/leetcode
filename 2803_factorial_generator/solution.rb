# LeetCode 2803 - Factorial Generator
# https://leetcode.com/problems/factorial-generator/

# @param {Integer} n
# @return {Integer[]}
def factorial_generator(n)
  cur = 1
  return [1] if n == 0
  (1..n).map do |i|
    cur *= i
    cur
  end
end
