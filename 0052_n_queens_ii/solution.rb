# LeetCode 0052 - N-Queens II
# https://leetcode.com/problems/n-queens-ii/

# @param {Integer} n
# @return {Integer}
def total_n_queens(n)
  count = 0
  cols = {}
  diag1 = {}
  diag2 = {}

  backtrack = lambda do |row|
    if row == n
      count += 1
      return
    end

    (0...n).each do |col|
      next if cols[col] || diag1[row + col] || diag2[row - col]

      cols[col] = true
      diag1[row + col] = true
      diag2[row - col] = true
      backtrack.call(row + 1)
      cols.delete(col)
      diag1.delete(row + col)
      diag2.delete(row - col)
    end
  end

  backtrack.call(0)
  count
end
