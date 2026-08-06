# LeetCode 1131 - Maximum of Absolute Value Expression
# https://leetcode.com/problems/maximum-of-absolute-value-expression/

# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer}
def max_abs_val_expr(arr1, arr2)
  n = arr1.length
  ans = 0
  [[1, 1], [1, -1], [-1, 1], [-1, -1]].each do |p, q|
    best = p * arr1[0] + q * arr2[0]
    (1...n).each do |i|
      cur = p * arr1[i] + q * arr2[i] + i
      ans = [ans, cur - best].max
      best = [best, p * arr1[i] + q * arr2[i] + i].min
    end
  end
  ans
end
