# LeetCode 0155 - Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack
  def initialize
    @values = []
    @minimums = []
  end

  def push(val)
    @values << val
    @minimums << [val, @minimums.last || val].min
  end

  def pop
    @values.pop
    @minimums.pop
  end

  def top
    @values.last
  end

  def get_min
    @minimums.last
  end
end