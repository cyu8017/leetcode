# LeetCode 1011 - Capacity To Ship Packages Within D Days
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

# @param {Integer[]} weights
# @param {Integer} days
# @return {Integer}
def ship_within_days(weights, days)
  lo = weights.max
  hi = weights.sum
  can = lambda do |cap|
    need = 1
    cur = 0
    weights.each do |w|
      if cur + w > cap
        need += 1
        cur = 0
      end
      cur += w
    end
    need <= days
  end
  while lo < hi
    mid = (lo + hi) / 2
    if can.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
