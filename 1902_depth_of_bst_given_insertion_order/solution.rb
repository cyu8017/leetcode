# LeetCode 1902 - Depth of BST Given Insertion Order
# https://leetcode.com/problems/depth-of-bst-given-insertion-order/

# @param {Integer[]} order
# @return {Integer}
def max_depth_bst(order)
  nodes = []
  ans = 0
  order.each do |value|
    lo = 0
    hi = nodes.length
    while lo < hi
      mid = (lo + hi) / 2
      if nodes[mid][0] < value
        lo = mid + 1
      else
        hi = mid
      end
    end
    i = lo
    depth = 1
    depth = [depth, nodes[i - 1][1] + 1].max if i.positive?
    depth = [depth, nodes[i][1] + 1].max if i < nodes.length
    nodes.insert(i, [value, depth])
    ans = [ans, depth].max
  end
  ans
end
