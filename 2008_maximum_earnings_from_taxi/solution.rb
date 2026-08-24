# LeetCode 2008 - Maximum Earnings From Taxi
# https://leetcode.com/problems/maximum-earnings-from-taxi/

# @param {Integer} n
# @param {Integer[][]} rides
# @return {Integer}
def max_taxi_earnings(n, rides)
  rides.sort_by! { |r| r[1] }
  m = rides.length
  ends = rides.map { |r| r[1] }
  dp = Array.new(m + 1, 0)
  rides.each_with_index do |(start, finish, tip), i|
    earn = finish - start + tip
    lo = 0
    hi = m
    while lo < hi
      mid = (lo + hi) >> 1
      if ends[mid] <= start
        lo = mid + 1
      else
        hi = mid
      end
    end
    dp[i + 1] = [dp[i], earn + dp[lo]].max
  end
  dp[m]
end
