# LeetCode 1130 - Minimum Cost Tree From Leaf Values
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

# @param {Integer[]} arr
# @return {Integer}
def mct_from_leaf_values(arr)
  stack = [Float::INFINITY]
  ans = 0
  arr.each do |x|
    while stack[-1] <= x
      mid = stack.pop
      ans += mid * [stack[-1], x].min
    end
    stack << x
  end
  while stack.length > 2
    ans += stack.pop * stack[-1]
  end
  ans
end
