# LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

# @param {Integer} upper
# @param {Integer} lower
# @param {Integer[]} colsum
# @return {Integer[][]}
def reconstruct_matrix(upper, lower, colsum)
  top = Array.new(colsum.length, 0)
  bottom = Array.new(colsum.length, 0)
  colsum.each_with_index do |value, i|
    next unless value == 2
    top[i] = bottom[i] = 1
    upper -= 1
    lower -= 1
  end
  return [] if upper < 0 || lower < 0
  colsum.each_with_index do |value, i|
    next unless value == 1
    if upper > 0
      top[i] = 1
      upper -= 1
    elsif lower > 0
      bottom[i] = 1
      lower -= 1
    else
      return []
    end
  end
  upper == 0 && lower == 0 ? [top, bottom] : []
end
