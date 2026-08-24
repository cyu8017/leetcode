# LeetCode 2604 - Minimum Time to Eat All Grains
# https://leetcode.com/problems/minimum-time-to-eat-all-grains/

# @param {Integer[]} hens
# @param {Integer[]} grains
# @return {Integer}
def minimum_time(hens, grains)
  hens = hens.sort
  grains = grains.sort

  ok = lambda do |t|
    j = 0
    hens.each do |h|
      return true if j >= grains.length

      if grains[j] >= h
        j += 1 while j < grains.length && grains[j] - h <= t
      else
        return false if h - grains[j] > t

        left = h - grains[j]
        max_right1 = t - 2 * left
        max_right2 = (t - left) / 2
        reach = h
        if max_right1 > max_right2
          reach = h + max_right1 if max_right1 > 0
        elsif max_right2 > 0
          reach = h + max_right2
        end
        j += 1 while j < grains.length && grains[j] <= reach
      end
    end
    j >= grains.length
  end

  lo = 0
  hi = 2_000_000_000
  while lo < hi
    mid = lo + (hi - lo) / 2
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end

alias solve minimum_time
