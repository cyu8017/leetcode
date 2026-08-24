# LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

# @param {Integer} n
# @param {Integer[]} quantities
# @return {Integer}
def minimized_maximum(n, quantities)
  can = lambda do |x|
    need = 0
    quantities.each do |q|
      need += (q + x - 1) / x
      return false if need > n
    end
    true
  end
  lo = 1
  hi = quantities.max
  while lo < hi
    mid = (lo + hi) >> 1
    if can.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
