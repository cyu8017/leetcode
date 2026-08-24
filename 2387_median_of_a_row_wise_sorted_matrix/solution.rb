# LeetCode 2387 - Median of a Row Wise Sorted Matrix
# https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

# @param {Integer[][]} grid
# @return {Integer}
def matrix_median(grid)
  m = grid.length
  n = grid[0].length
  lo = 1
  hi = 1_000_000
  need = (m * n) / 2 + 1
  count_le = lambda do |x|
    cnt = 0
    grid.each do |row|
      l = 0
      r = n
      while l < r
        mid = (l + r) >> 1
        if row[mid] <= x
          l = mid + 1
        else
          r = mid
        end
      end
      cnt += l
    end
    cnt
  end
  while lo < hi
    mid = (lo + hi) >> 1
    if count_le.call(mid) >= need
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end

alias solve matrix_median
