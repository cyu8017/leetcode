# LeetCode 3225 - Maximum Score From Grid Operations
# https://leetcode.com/problems/maximum-score-from-grid-operations/

# @param {Integer[][]} grid
# @return {Integer}
def maximum_score(grid)
  n = grid.length
  prefix = Array.new(n) { Array.new(n + 1, 0) }
  (0...n).each do |j|
    (0...n).each { |i| prefix[j][i + 1] = prefix[j][i] + grid[i][j] }
  end
  prev_pick = Array.new(n + 1, 0)
  prev_skip = Array.new(n + 1, 0)
  (1...n).each do |j|
    curr_pick = Array.new(n + 1, 0)
    curr_skip = Array.new(n + 1, 0)
    (0..n).each do |curr|
      (0..n).each do |prev|
        if curr > prev
          score = prefix[j - 1][curr] - prefix[j - 1][prev]
          curr_pick[curr] = [curr_pick[curr], prev_skip[prev] + score].max
          curr_skip[curr] = [curr_skip[curr], prev_skip[prev] + score].max
        else
          score = prefix[j][prev] - prefix[j][curr]
          curr_pick[curr] = [curr_pick[curr], prev_pick[prev] + score].max
          curr_skip[curr] = [curr_skip[curr], prev_pick[prev]].max
        end
      end
    end
    prev_pick = curr_pick
    prev_skip = curr_skip
  end
  prev_pick.max
end
