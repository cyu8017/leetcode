# LeetCode 2500 - Delete Greatest Value in Each Row
# https://leetcode.com/problems/delete-greatest-value-in-each-row/

# @param {Integer[][]} grid
# @return {Integer}
def delete_greatest_value(grid)
  grid.each(&:sort!)
  ans = 0
  n = grid[0].length
  (0...n).each do |c|
    mx = 0
    grid.each { |row| mx = row[c] if row[c] > mx }
    ans += mx
  end
  ans
end
