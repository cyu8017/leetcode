# LeetCode 1231 - Divide Chocolate
# https://leetcode.com/problems/divide-chocolate/

# @param {Integer[]} sweetness
# @param {Integer} k
# @return {Integer}
def maximize_sweetness(sweetness, k)
  lo = 1
  hi = sweetness.sum / (k + 1)
  while lo <= hi
    mid = (lo + hi) / 2
    pieces = 0
    current = 0
    sweetness.each do |value|
      current += value
      if current >= mid
        pieces += 1
        current = 0
      end
    end
    if pieces >= k + 1
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  hi
end
