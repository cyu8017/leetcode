# LeetCode 1954 - Minimum Garden Perimeter to Collect Enough Apples
# https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

# @param {Integer} needed_apples
# @return {Integer}
def minimum_perimeter(needed_apples)
  lo = 1
  hi = 100_000
  while lo < hi
    mid = (lo + hi) / 2
    apples = 2 * mid * (mid + 1) * (2 * mid + 1)
    if apples >= needed_apples
      hi = mid
    else
      lo = mid + 1
    end
  end
  8 * lo
end
