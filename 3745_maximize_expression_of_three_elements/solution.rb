# LeetCode 3745 - Maximize Expression of Three Elements
# https://leetcode.com/problems/maximize-expression-of-three-elements/

# @param {Integer[]} nums
# @return {Integer}
def maximize_expression_of_three(nums)
  inf = 1 << 30
  a = -inf
  b = -inf
  c = inf
  nums.each do |x|
    c = x if x < c
    if x >= a
      b = a
      a = x
    elsif x > b
      b = x
    end
  end
  a + b - c
end
