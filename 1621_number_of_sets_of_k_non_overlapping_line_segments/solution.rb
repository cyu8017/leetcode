# LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

def _comb_1621(n, k)
  return 0 if k < 0 || k > n
  return 1 if k.zero? || k == n

  k = n - k if k > n - k
  res = 1
  (1..k).each do |i|
    res = res * (n - k + i) / i
  end
  res
end

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def number_of_sets(n, k)
  _comb_1621(n + k - 1, 2 * k) % 1_000_000_007
end
