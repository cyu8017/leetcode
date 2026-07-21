# LeetCode 1891 - Cutting Ribbons
# https://leetcode.com/problems/cutting-ribbons/

# @param {Integer[]} ribbons
# @param {Integer} k
# @return {Integer}
def max_length(ribbons, k)
  can = lambda { |length| ribbons.sum { |ribbon| ribbon / length } >= k }

  lo = 1
  hi = ribbons.max
  while lo < hi
    mid = (lo + hi + 1) / 2
    if can.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  can.call(lo) ? lo : 0
end
