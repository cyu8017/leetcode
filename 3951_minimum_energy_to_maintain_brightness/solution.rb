# LeetCode 3951 - Minimum Energy To Maintain Brightness
# https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

# @param {Integer} n
# @param {Integer} brightness
# @param {Integer[][]} intervals
# @return {Integer}
def min_energy(n, brightness, intervals)
  intervals.sort_by! { |a| a[0] }
  merged = [[intervals[0][0], intervals[0][1]]]
  (1...intervals.length).each do |i|
    x = intervals[i]
    last = merged[-1]
    if last[1] < x[0]
      merged << [x[0], x[1]]
    elsif x[1] > last[1]
      last[1] = x[1]
    end
  end
  ans = 0
  merged.each do |interval|
    m = interval[1] - interval[0] + 1
    ans += ((brightness + 2) / 3) * m
  end
  ans
end
