# LeetCode 2594 - Minimum Time to Repair Cars
# https://leetcode.com/problems/minimum-time-to-repair-cars/

# @param {Integer[]} ranks
# @param {Integer} cars
# @return {Integer}
def repair_cars(ranks, cars)
  mn = ranks.min
  lo = 1
  hi = mn * cars * cars

  ok = lambda do |t|
    done = 0
    ranks.each do |r|
      l = 0
      h = cars
      while l < h
        mid = (l + h + 1) / 2
        if r * mid * mid <= t
          l = mid
        else
          h = mid - 1
        end
      end
      done += l
      return true if done >= cars
    end
    done >= cars
  end

  while lo < hi
    mid = (lo + hi) / 2
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
