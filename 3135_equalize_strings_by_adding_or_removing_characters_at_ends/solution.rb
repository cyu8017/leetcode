# LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
# https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

# @param {String} initial
# @param {String} target
# @return {Integer}
def min_operations(initial, target)
  m = initial.length
  n = target.length
  f = Array.new(m + 1) { Array.new(n + 1, 0) }
  mx = 0
  m.times do |i|
    n.times do |j|
      if initial[i] == target[j]
        f[i + 1][j + 1] = f[i][j] + 1
        mx = [mx, f[i + 1][j + 1]].max
      end
    end
  end
  m + n - 2 * mx
end
