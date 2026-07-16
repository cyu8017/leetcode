# LeetCode 0108 - Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {Integer[]} nums
# @return {TreeNode}
def sorted_array_to_bst(nums)
  build = lambda do |left, right|
    return nil if left > right

    mid = (left + right + 1) / 2
    root = TreeNode.new(nums[mid])
    root.left = build.call(left, mid - 1)
    root.right = build.call(mid + 1, right)
    root
  end

  build.call(0, nums.length - 1)
end
