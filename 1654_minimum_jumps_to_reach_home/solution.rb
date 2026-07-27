# LeetCode 1654 - Minimum Jumps to Reach Home
# https://leetcode.com/problems/minimum-jumps-to-reach-home/

# @param {Integer[]} forbidden
# @param {Integer} a
# @param {Integer} b
# @param {Integer} x
# @return {Integer}
def minimum_jumps(forbidden, a, b, x)
  bad = forbidden.to_h { |v| [v, true] }
  limit = ([x] + forbidden).max + a + b
  q = [[0, 0, false]]
  seen = { [0, false] => true }
  until q.empty?
    pos, dist, back = q.shift
    return dist if pos == x

    [[pos + a, false], [pos - b, true]].each do |np, nb|
      next if np.negative? || np > limit || bad[np] || seen[[np, nb]] || (back && nb)

      seen[[np, nb]] = true
      q << [np, dist + 1, nb]
    end
  end
  -1
end
