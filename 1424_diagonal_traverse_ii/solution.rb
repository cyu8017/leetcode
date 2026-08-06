# LeetCode 1424 - Diagonal Traverse Ii
# https://leetcode.com/problems/diagonal-traverse-ii/

def find_diagonal_order(nums)
  diagonals = {}
  nums.each_with_index do |values, row|
    values.each_with_index do |value, col|
      (diagonals[row + col] ||= []) << value
    end
  end
  diagonals.keys.sort.flat_map { |key| diagonals[key].reverse }
end
