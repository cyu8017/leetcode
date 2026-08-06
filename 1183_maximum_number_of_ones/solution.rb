# LeetCode 1183 - Maximum Number of Ones
# https://leetcode.com/problems/maximum-number-of-ones/

# @param {Integer} width
# @param {Integer} height
# @param {Integer} side_length
# @param {Integer} max_ones
# @return {Integer}
def maximum_number_of_ones(width, height, side_length, max_ones)
  counts = []
  side_length.times do |r|
    side_length.times do |c|
      rows = (height - r + side_length - 1) / side_length
      cols = (width - c + side_length - 1) / side_length
      counts << rows * cols
    end
  end
  counts.sort.reverse[0...max_ones].sum
end
