# LeetCode 2732 - Find a Good Subset of the Matrix
# https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

# @param {Integer[][]} grid
# @return {Integer[]}
def good_subsetof_binary_matrix(grid)
  n = grid[0].length
  first = {}
  grid.each_with_index do |row, i|
    mask = 0
    (0...n).each { |j| mask |= 1 << j if row[j] == 1 }
    return [i] if mask == 0
    first.each do |pm, idx|
      if (pm & mask) == 0
        return idx < i ? [idx, i] : [i, idx]
      end
    end
    first[mask] = i unless first.key?(mask)
  end
  []
end
