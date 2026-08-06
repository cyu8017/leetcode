# LeetCode 1289 - Minimum Falling Path Sum II
# https://leetcode.com/problems/minimum-falling-path-sum-ii/

# @param {Integer[][]} grid
# @return {Integer}
def min_falling_path_sum(grid)
  dp = grid[0].dup
  grid[1..].each do |row|
    first = (0...dp.length).min_by { |i| dp[i] }
    second_value = dp.length > 1 ? (0...dp.length).reject { |i| i == first }.map { |i| dp[i] }.min : 0
    dp = row.each_with_index.map { |value, i| value + (i == first ? second_value : dp[first]) }
  end
  dp.min
end
