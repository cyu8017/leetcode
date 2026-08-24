# LeetCode 2583 - Kth Largest Sum in a Binary Tree
# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def kth_largest_level_sum(root, k)
  return -1 if root.nil?

  sums = []
  q = [root]
  until q.empty?
    sz = q.length
    s = 0
    sz.times do
      node = q.shift
      s += node.val
      q << node.left if node.left
      q << node.right if node.right
    end
    sums << s
  end
  sums.sort!.reverse!
  return -1 if k > sums.length

  sums[k - 1]
end
