# LeetCode 0539 - Minimum Time Difference
# https://leetcode.com/problems/minimum-time-difference/

class Solution
  def find_min_difference(time_points)
    minutes = time_points.map do |time|
      hour, minute = time.split(":").map(&:to_i)
      hour * 60 + minute
    end
    minutes.sort!

    best = minutes[-1] - minutes[0]
    (1...minutes.length).each do |i|
      best = [best, minutes[i] - minutes[i - 1]].min
    end
    [best, 24 * 60 - minutes[-1] + minutes[0]].min
  end

  alias_method :findMinDifference, :find_min_difference
end
