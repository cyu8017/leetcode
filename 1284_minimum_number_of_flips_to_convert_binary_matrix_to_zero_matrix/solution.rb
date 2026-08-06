# LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

require "set"

# @param {Integer[][]} mat
# @return {Integer}
def min_flips(mat)
  m = mat.length
  n = mat[0].length
  start = 0
  m.times { |r| n.times { |c| start |= mat[r][c] << (r * n + c) } }
  masks = []
  m.times do |r|
    n.times do |c|
      mask = 0
      [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
        nr = r + dr
        nc = c + dc
        mask ^= 1 << (nr * n + nc) if nr.between?(0, m - 1) && nc.between?(0, n - 1)
      end
      masks << mask
    end
  end
  queue = [[start, 0]]
  seen = Set[start]
  until queue.empty?
    state, distance = queue.shift
    return distance if state == 0
    masks.each do |mask|
      nxt = state ^ mask
      next if seen.include?(nxt)
      seen.add(nxt)
      queue << [nxt, distance + 1]
    end
  end
  -1
end
