# LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
# https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def count_sorted_matrices(grid, k)
  m = grid.length
  n = grid[0].length
  ans = 0
  m.times do |r1|
    (r1...m).each do |r2|
      n.times do |c1|
        (c1...n).each do |c2|
          good = true
          i = r1
          while i <= r2 && good
            (c1..c2).each do |j|
              if grid[i][j] > k
                good = false
                break
              end
              if j > c1 && grid[i][j] < grid[i][j - 1]
                good = false
                break
              end
              if i > r1 && grid[i][j] < grid[i - 1][j]
                good = false
                break
              end
            end
            i += 1
          end
          ans += 1 if good
        end
      end
    end
  end
  ans
end
