# LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
# https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

# @param {Integer} k
# @return {Integer}
def min_operations(k)
  ans = k
  k.times do |a|
    x = a + 1
    b = (k + x - 1) / x - 1
    ans = [ans, a + b].min
  end
  ans
end
