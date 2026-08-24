# LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

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
# @return {Integer[]}
def tree_queries(root, queries)
  height = {}
  level = {}
  level_max = {}

  dfs = lambda do |node, d|
    return -1 if node.nil?

    level[node.val] = d
    h = 1 + [dfs.call(node.left, d + 1), dfs.call(node.right, d + 1)].max
    height[node.val] = h
    arr = level_max[d]
    if arr.nil?
      arr = []
      level_max[d] = arr
    end
    if arr.empty?
      arr << h
    elsif h >= arr[0]
      if arr.length == 1
        arr << arr[0]
      else
        arr[1] = arr[0]
      end
      arr[0] = h
    elsif arr.length == 1 || h > arr[1]
      if arr.length == 1
        arr << h
      else
        arr[1] = h
      end
    end
    h
  end

  dfs.call(root, 0)
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    d = level[q]
    h = height[q]
    top = level_max[d]
    ans[i] = if top[0] == h
               top.length > 1 ? d + top[1] : d - 1
             else
               d + top[0]
             end
  end
  ans
end
