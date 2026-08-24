# LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
# https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer[]} queries
# @return {Integer[][]}
def closest_nodes(root, queries)
  vals = []
  inorder = lambda do |node|
    return if node.nil?

    inorder.call(node.left)
    vals << node.val
    inorder.call(node.right)
  end
  inorder.call(root)

  lower_bound = lambda do |q|
    lo = 0
    hi = vals.length
    while lo < hi
      mid = (lo + hi) >> 1
      if vals[mid] < q
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  ans = []
  queries.each do |q|
    j = lower_bound.call(q)
    mx = j < vals.length ? vals[j] : -1
    mn = -1
    if j < vals.length && vals[j] == q
      mn = q
    elsif j > 0
      mn = vals[j - 1]
    end
    ans << [mn, mx]
  end
  ans
end
