# LeetCode 3218 - Minimum Cost for Cutting Cake I
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[]} horizontal_cut
# @param {Integer[]} vertical_cut
# @return {Integer}
def minimum_cost(m, n, horizontal_cut, vertical_cut)
  horizontal_cut.sort! { |a, b| b <=> a }
  vertical_cut.sort! { |a, b| b <=> a }
  i = j = 0
  h = v = 1
  ans = 0
  while i < m - 1 || j < n - 1
    if j == n - 1 || (i < m - 1 && horizontal_cut[i] > vertical_cut[j])
      ans += horizontal_cut[i] * v
      h += 1
      i += 1
    else
      ans += vertical_cut[j] * h
      v += 1
      j += 1
    end
  end
  ans
end
