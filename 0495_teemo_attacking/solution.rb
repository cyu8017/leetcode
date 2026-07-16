# LeetCode 0495 - Teemo Attacking
# https://leetcode.com/problems/teemo-attacking/

class Solution
  def find_poisoned_duration(time_series, duration)
    return 0 if time_series.empty?

    total = duration
    (1...time_series.length).each do |index|
      total += [duration, time_series[index] - time_series[index - 1]].min
    end
    total
  end

  alias_method :findPoisonedDuration, :find_poisoned_duration
end
