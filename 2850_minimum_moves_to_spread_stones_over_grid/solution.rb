# LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
# https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_moves(grid)
  extras = []
  zeros = []
  (0...3).each do |i|
    (0...3).each do |j|
      if grid[i][j] == 0
        zeros << [i, j]
      elsif grid[i][j] > 1
        (grid[i][j] - 1).times { extras << [i, j] }
      end
    end
  end
  return 0 if zeros.empty?

  best = 1 << 30
  dfs = lambda do |i, cost|
    return if cost >= best
    if i == zeros.length
      best = cost
      return
    end
    extras.each_with_index do |e, j|
      next if e[0] < 0

      extras[j] = [-1, e[1]]
      d = (e[0] - zeros[i][0]).abs + (e[1] - zeros[i][1]).abs
      dfs.call(i + 1, cost + d)
      extras[j] = e
    end
  end
  dfs.call(0, 0)
  best
end
