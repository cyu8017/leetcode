# LeetCode 2526 - Find Consecutive Integers from a Data Stream
# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream
  def initialize(value, k)
    @value = value
    @k = k
    @streak = 0
  end

  def consec(num)
    if num == @value
      @streak += 1
    else
      @streak = 0
    end
    @streak >= @k
  end
end
