# LeetCode 2528 - Maximize the Minimum Powered City
# https://leetcode.com/problems/maximize-the-minimum-powered-city/

# @param {Integer[]} stations
# @param {Integer} r
# @param {Integer} k
# @return {Integer}
def max_power(stations, r, k)
  n = stations.length
  diff = Array.new(n + 1, 0)
  n.times do |i|
    left = [0, i - r].max
    right = [n - 1, i + r].min
    diff[left] += stations[i]
    diff[right + 1] -= stations[i]
  end
  power = Array.new(n, 0)
  cur = 0
  n.times do |i|
    cur += diff[i]
    power[i] = cur
  end
  lo = 0
  hi = k
  power.each { |p| hi = p if p > hi }
  hi += k

  ok = lambda do |x|
    extra = Array.new(n + 1, 0)
    have = 0
    used = 0
    n.times do |i|
      have += extra[i]
      need = x - (power[i] + have)
      if need > 0
        used += need
        return false if used > k

        have += need
        endi = i + 2 * r
        extra[endi + 1] -= need if endi + 1 <= n
      end
    end
    true
  end

  while lo < hi
    mid = (lo + hi + 1) / 2
    if ok.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
