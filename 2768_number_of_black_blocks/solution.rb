# LeetCode 2768 - Number of Black Blocks
# https://leetcode.com/problems/number-of-black-blocks/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} coordinates
# @return {Integer[]}
def count_black_blocks(m, n, coordinates)
  cnt = Hash.new(0)
  coordinates.each do |x, y|
    ((x - 1)..x).each do |i|
      ((y - 1)..y).each do |j|
        cnt[[i, j]] += 1 if i >= 0 && i < m - 1 && j >= 0 && j < n - 1
      end
    end
  end
  out = Array.new(5, 0)
  out[0] = (m - 1) * (n - 1)
  cnt.each_value do |v|
    out[v] += 1
    out[0] -= 1
  end
  out
end
