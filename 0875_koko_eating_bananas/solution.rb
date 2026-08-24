# LeetCode 0875 - Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

# @param {Integer[]} piles
# @param {Integer} h
# @return {Integer}
def min_eating_speed(piles, h)
  lo = 1
  hi = piles.max
  while lo < hi
    mid = (lo + hi) / 2
    hours = piles.sum { |p| (p + mid - 1) / mid }
    if hours <= h
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
