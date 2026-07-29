# LeetCode 1001 - Grid Illumination
# https://leetcode.com/problems/grid-illumination/

# @param {Integer} n
# @param {Integer[][]} lamps
# @param {Integer[][]} queries
# @return {Integer[]}
def grid_illumination(n, lamps, queries)
  rows = Hash.new(0)
  cols = Hash.new(0)
  diag1 = Hash.new(0)
  diag2 = Hash.new(0)
  lit = {}
  lamps.each do |r, c|
    key = [r, c]
    next if lit[key]

    lit[key] = true
    rows[r] += 1
    cols[c] += 1
    diag1[r - c] += 1
    diag2[r + c] += 1
  end

  ans = []
  queries.each do |r, c|
    ans << ((rows[r] > 0 || cols[c] > 0 || diag1[r - c] > 0 || diag2[r + c] > 0) ? 1 : 0)
    ((r - 1)..(r + 1)).each do |i|
      ((c - 1)..(c + 1)).each do |j|
        key = [i, j]
        next unless lit[key]

        lit.delete(key)
        rows[i] -= 1
        cols[j] -= 1
        diag1[i - j] -= 1
        diag2[i + j] -= 1
      end
    end
  end
  ans
end
