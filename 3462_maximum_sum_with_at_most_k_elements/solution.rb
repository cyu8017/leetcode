# LeetCode 3462 - Maximum Sum With at Most K Elements
# https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

# @param {Integer[][]} grid
# @param {Integer[]} limits
# @param {Integer} k
# @return {Integer}
def max_sum(grid, limits, k)
  h = []
  s = 0
  (0...grid.length).each do |i|
    r = grid[i].sort
    lim = limits[i]
    lim = r.length if lim > r.length
    (0...lim).each do |j|
      val = r[r.length - 1 - j]
      h << val
      h.sort!
      s += val
      s -= h.shift if h.length > k
    end
  end
  s
end
