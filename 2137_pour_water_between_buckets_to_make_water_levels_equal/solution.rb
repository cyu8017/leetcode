# LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
# https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

# @param {Integer[]} buckets
# @param {Integer} loss
# @return {Float}
def equalize_water(buckets, loss)
  lo = 0.0
  hi = buckets.max.to_f
  60.times do
    mid = (lo + hi) / 2.0
    have = 0.0
    need = 0.0
    buckets.each do |b|
      if b >= mid
        have += b - mid
      else
        need += mid - b
      end
    end
    if have * (1 - loss / 100.0) >= need
      lo = mid
    else
      hi = mid
    end
  end
  lo
end
