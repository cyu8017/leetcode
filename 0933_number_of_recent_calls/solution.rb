# LeetCode 0933 - Number of Recent Calls
# https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter
  def initialize
    @q = []
  end

  def ping(t)
    @q << t
    @q.shift while @q[0] < t - 3000
    @q.length
  end
end
