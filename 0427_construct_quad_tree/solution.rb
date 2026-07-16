# LeetCode 0427 - Construct Quad Tree
# https://leetcode.com/problems/construct-quad-tree/

class Node
  attr_accessor :val, :isLeaf, :topLeft, :topRight, :bottomLeft, :bottomRight

  def initialize(val = false, is_leaf = false, top_left = nil, top_right = nil, bottom_left = nil, bottom_right = nil)
    @val = val
    @isLeaf = is_leaf
    @topLeft = top_left
    @topRight = top_right
    @bottomLeft = bottom_left
    @bottomRight = bottom_right
  end
end

class Solution
  def construct(grid)
    build = lambda do |row, col, size|
      if size == 1
        return Node.new(grid[row][col] == 1, true)
      end

      half = size / 2
      top_left = build.call(row, col, half)
      top_right = build.call(row, col + half, half)
      bottom_left = build.call(row + half, col, half)
      bottom_right = build.call(row + half, col + half, half)

      if top_left.isLeaf && top_right.isLeaf && bottom_left.isLeaf && bottom_right.isLeaf &&
         top_left.val == top_right.val && top_left.val == bottom_left.val && top_left.val == bottom_right.val
        return Node.new(top_left.val, true)
      end

      Node.new(true, false, top_left, top_right, bottom_left, bottom_right)
    end

    build.call(0, 0, grid.length)
  end
end
