# LeetCode 1870 - Minimum Speed to Arrive on Time
# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

# @param {Integer[]} dist
# @param {Float} hour
# @return {Integer}
def min_speed_on_time(dist, hour)
  n = dist.length
  return -1 if n - 1 >= hour

  can_arrive = lambda do |speed|
    time = 0.0
    (0...n - 1).each do |i|
      time += (dist[i] + speed - 1) / speed
    end
    time += dist[-1].to_f / speed
    time <= hour
  end

  return -1 unless can_arrive.call(10**7)

  lo = 1
  hi = 10**7
  while lo < hi
    mid = (lo + hi) / 2
    if can_arrive.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
