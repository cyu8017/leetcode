# LeetCode 0272 - Closest Binary Search Tree Value II
# https://leetcode.com/problems/closest-binary-search-tree-value-ii/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Float} target
# @param {Integer} k
# @return {Integer[]}
def closest_k_values(root, target, k)
  values = []

  inorder = lambda do |node|
    return if node.nil?

    inorder.call(node.left)
    values << node.val
    inorder.call(node.right)
  end
  inorder.call(root)

  lo = 0
  hi = values.length
  while lo < hi
    mid = (lo + hi) / 2
    if values[mid] < target
      lo = mid + 1
    else
      hi = mid
    end
  end

  left = lo - 1
  right = lo
  result = []
  while result.length < k
    if right >= values.length ||
       (left >= 0 && (values[left] - target).abs <= (values[right] - target).abs)
      result << values[left]
      left -= 1
    else
      result << values[right]
      right += 1
    end
  end
  result
end
