# LeetCode 0774 - Minimize Max Distance to Gas Station
# https://leetcode.com/problems/minimize-max-distance-to-gas-station/

# @param {Integer[]} stations
# @param {Integer} k
# @return {Float}
def minmax_gas_dist(stations, k)
  can = lambda do |dist|
    needed = 0
    (1...stations.length).each do |i|
      needed += ((stations[i] - stations[i - 1]) / dist).to_i
    end
    needed <= k
  end

  lo = 0.0
  hi = (stations[-1] - stations[0]).to_f
  while hi - lo > 1e-6
    mid = (lo + hi) / 2.0
    if can.call(mid)
      hi = mid
    else
      lo = mid
    end
  end
  hi
end
