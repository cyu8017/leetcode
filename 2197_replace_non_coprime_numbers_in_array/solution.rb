# LeetCode 2197 - Replace Non-Coprime Numbers in Array
# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

# @param {Integer[]} nums
# @return {Integer[]}
def replace_non_coprimes(nums)
  stack = []
  nums.each do |x0|
    x = x0
    while !stack.empty?
      g = gcd(stack[-1], x)
      break if g == 1

      x = stack[-1] / g * x
      stack.pop
    end
    stack << x
  end
  stack
end

def gcd(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end
