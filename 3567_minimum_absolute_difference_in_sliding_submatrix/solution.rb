# LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer[][]}
def min_abs_diff(grid, k)
  m = grid.length
  n = grid[0].length
  ans = Array.new(m - k + 1) { Array.new(n - k + 1, 0) }
  (0..(m - k)).each do |i|
    (0..(n - k)).each do |j|
      nums = []
      (i...(i + k)).each { |x| (j...(j + k)).each { |y| nums << grid[x][y] } }
      nums.sort!
      d = 2147483647
      (1...nums.length).each do |t|
        d = [d, (nums[t] - nums[t - 1]).abs].min if nums[t] != nums[t - 1]
      end
      ans[i][j] = d if d != 2147483647
    end
  end
  ans
end
