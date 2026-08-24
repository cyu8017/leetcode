# LeetCode 0654 - Maximum Binary Tree
# https://leetcode.com/problems/maximum-binary-tree/

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
def construct_maximum_binary_tree(nums)
  build = lambda do |left, right|
    return nil if left > right

    mid = left
    (left..right).each { |i| mid = i if nums[i] > nums[mid] }
    TreeNode.new(nums[mid], build.call(left, mid - 1), build.call(mid + 1, right))
  end

  build.call(0, nums.length - 1)
end
