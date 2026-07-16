# LeetCode 0346 - Moving Average from Data Stream
# https://leetcode.com/problems/moving-average-from-data-stream/

class MovingAverage
  def initialize(size)
    @size = size
    @values = []
    @total = 0
  end

  def next(val)
    @values.push(val)
    @total += val
    if @values.length > @size
      @total -= @values.shift
    end
    @total.to_f / @values.length
  end
end
