# LeetCode 3893 - Maximum Team Size with Overlapping Intervals
# https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

# @param {Integer[]} start_time
# @param {Integer[]} end_time
# @return {Integer}
def maximum_team_size(start_time, end_time)
  upper_bound = lambda do |a, x|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) / 2
      if a[mid] <= x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  n = start_time.length
  st = start_time.sort
  en = end_time.sort
  ans = 0
  n.times do |t|
    l = start_time[t]
    r = end_time[t]
    i = upper_bound.call(en, l - 1)
    j = upper_bound.call(st, r)
    ans = [ans, j - i].max
  end
  ans
end
