# LeetCode 1901 - Find a Peak Element II
# https://leetcode.com/problems/find-a-peak-element-ii/

# @param {Integer[][]} mat
# @return {Integer[]}
def find_peak_grid(mat)
  rows = mat.length
  cols = mat[0].length
  lo = 0
  hi = cols - 1
  while lo <= hi
    mid = (lo + hi) / 2
    max_row = (0...rows).max_by { |r| mat[r][mid] }
    left = mid.positive? ? mat[max_row][mid - 1] : -1
    right = mid + 1 < cols ? mat[max_row][mid + 1] : -1
    return [max_row, mid] if mat[max_row][mid] >= left && mat[max_row][mid] >= right
    if left > mat[max_row][mid]
      hi = mid - 1
    else
      lo = mid + 1
    end
  end
  [0, 0]
end
