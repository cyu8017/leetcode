# LeetCode 1751 - Maximum Number of Events That Can Be Attended II
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

# @param {Integer[][]} events
# @param {Integer} k
# @return {Integer}
def max_value(events, k)
  events = events.sort
  n = events.length
  starts = events.map { |e| e[0] }

  upper_bound = lambda do |target|
    lo = 0
    hi = n
    while lo < hi
      mid = (lo + hi) / 2
      if starts[mid] <= target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  dp = Array.new(k + 1) { Array.new(n + 1, 0) }
  (n - 1).downto(0) do |i|
    j = upper_bound.call(events[i][1])
    (1..k).each do |remain|
      dp[remain][i] = [dp[remain][i + 1], events[i][2] + dp[remain - 1][j]].max
    end
  end
  dp[k][0]
end
