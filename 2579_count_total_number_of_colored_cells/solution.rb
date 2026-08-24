# LeetCode 2579 - Count Total Number of Colored Cells
# https://leetcode.com/problems/count-total-number-of-colored-cells/

# @param {Integer} n
# @return {Integer}
def colored_cells(n)
  1 + 2 * n * (n - 1)
end
