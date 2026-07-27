# LeetCode 1687 - Delivering Boxes from Storage to Ports
# https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

# @param {Integer[][]} boxes
# @param {Integer} ports_count
# @param {Integer} max_boxes
# @param {Integer} max_weight
# @return {Integer}
def box_delivering(boxes, ports_count, max_boxes, max_weight)
  n = boxes.length
  w = Array.new(n + 1, 0)
  changes = Array.new(n + 1, 0)
  boxes.each_with_index do |(p, wt), idx|
    i = idx + 1
    w[i] = w[i - 1] + wt
    changes[i] = changes[i - 1] + (i > 1 && p != boxes[i - 2][0] ? 1 : 0)
  end
  dp = Array.new(n + 1, 0)
  q = [0]
  (1..n).each do |i|
    q.shift while !q.empty? && (i - q[0] > max_boxes || w[i] - w[q[0]] > max_weight)
    j = q[0]
    dp[i] = dp[j] + changes[i] - changes[j + 1] + 2
    next if i >= n

    val = dp[i] - changes[i + 1]
    q.pop while !q.empty? && dp[q[-1]] - changes[q[-1] + 1] >= val
    q << i
  end
  dp[n]
end
