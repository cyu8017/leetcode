# LeetCode 2187 - Minimum Time to Complete Trips
# https://leetcode.com/problems/minimum-time-to-complete-trips/

# @param {Integer[]} time
# @param {Integer} total_trips
# @return {Integer}
def minimum_time(time, total_trips)
  mn = time.min
  lo = 1
  hi = mn * total_trips
  while lo < hi
    mid = (lo + hi) / 2
    trips = 0
    ok = false
    time.each do |t|
      trips += mid / t
      if trips >= total_trips
        ok = true
        break
      end
    end
    if ok
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
