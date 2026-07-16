# LeetCode 0417 - Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/

require "set"

class Solution
  def pacific_atlantic(heights)
    return [] if heights.empty? || heights[0].empty?

    rows = heights.length
    cols = heights[0].length
    pacific = Set.new
    atlantic = Set.new

    rows.times do |row|
      dfs(heights, row, 0, pacific, heights[row][0])
      dfs(heights, row, cols - 1, atlantic, heights[row][cols - 1])
    end
    cols.times do |col|
      dfs(heights, 0, col, pacific, heights[0][col])
      dfs(heights, rows - 1, col, atlantic, heights[rows - 1][col])
    end

    (pacific & atlantic).map { |row, col| [row, col] }
  end

  alias_method :pacificAtlantic, :pacific_atlantic

  private

  def dfs(heights, row, col, visited, previous)
    return if visited.include?([row, col])
    return if row.negative? || row >= heights.length || col.negative? || col >= heights[0].length
    return if heights[row][col] < previous

    visited.add([row, col])
    height = heights[row][col]
    dfs(heights, row + 1, col, visited, height)
    dfs(heights, row - 1, col, visited, height)
    dfs(heights, row, col + 1, visited, height)
    dfs(heights, row, col - 1, visited, height)
  end
end
