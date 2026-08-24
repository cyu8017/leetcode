# LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
# https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def kth_largest_perfect_subtree(root, k)
  sizes = []
  dfs = lambda do |node|
    return [0, 0, 1] if node.nil?

    left = dfs.call(node.left)
    right = dfs.call(node.right)
    sz = left[1] + right[1] + 1
    perf = left[2] == 1 && right[2] == 1 && left[0] == right[0]
    sizes << sz if perf
    [[left[0], right[0]].max + 1, sz, perf ? 1 : 0]
  end
  dfs.call(root)
  sizes.sort!.reverse!
  return -1 if k > sizes.length

  sizes[k - 1]
end
