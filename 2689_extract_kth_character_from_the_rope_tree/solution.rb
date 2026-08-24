# LeetCode 2689 - Extract Kth Character From The Rope Tree
# https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

class RopeTreeNode
  attr_accessor :len, :val, :left, :right

  def initialize(len = 0, val = "", left = nil, right = nil)
    @len = len
    @val = val
    @left = left
    @right = right
  end
end

# @param {RopeTreeNode} root
# @param {Integer} k
# @return {String}
def get_kth_character(root, k)
  dfs = nil
  dfs = lambda do |node, kk|
    return node.val if node.left.nil? && node.right.nil?

    left_len = 0
    if node.left
      left_len = node.left.len > 0 ? node.left.len : 1
    end
    return dfs.call(node.left, kk) if kk <= left_len

    dfs.call(node.right, kk - left_len)
  end
  dfs.call(root, k)
end

def solve(*args)
  get_kth_character(*args)
end
