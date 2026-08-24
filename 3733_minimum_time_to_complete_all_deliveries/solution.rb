# LeetCode 3733 - Minimum Time to Complete All Deliveries
# https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

# @param {Integer[]} d
# @param {Integer[]} r
# @return {Integer}
def minimum_time(d, r)
  ok = lambda do |t|
    w0 = t - t / r[0]
    w1 = t - t / r[1]
    w0 + w1 >= d[0] + d[1]
  end
  lo = 1
  hi = 10**18
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
