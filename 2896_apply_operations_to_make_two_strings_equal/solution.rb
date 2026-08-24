# LeetCode 2896 - Apply Operations to Make Two Strings Equal
# https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

# @param {String} s1
# @param {String} s2
# @param {Integer} x
# @return {Integer}
def min_operations(s1, s2, x)
  diff = []
  (0...s1.length).each { |i| diff << i if s1[i] != s2[i] }
  m = diff.length
  return -1 if m.odd?
  return 0 if m == 0

  inf = 1 << 30
  dp2 = Array.new(m + 1, inf)
  dp2[0] = 0
  (0...m).each do |i|
    next if dp2[i] >= inf
    next unless i + 1 < m

    cand = diff[i + 1] - diff[i]
    cand = x if cand > x
    dp2[i + 2] = dp2[i] + cand if dp2[i] + cand < dp2[i + 2]
  end
  dp2[m] >= inf ? -1 : dp2[m]
end
