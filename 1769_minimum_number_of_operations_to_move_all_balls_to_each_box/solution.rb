# LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

# @param {String} boxes
# @return {Integer[]}
def min_operations(boxes)
  n = boxes.length
  ans = Array.new(n, 0)
  balls = 0
  ops = 0
  (1...n).each do |i|
    balls += boxes[i - 1].to_i
    ops += balls
    ans[i] = ops
  end
  balls = 0
  ops = 0
  (n - 2).downto(0) do |i|
    balls += boxes[i + 1].to_i
    ops += balls
    ans[i] += ops
  end
  ans
end
