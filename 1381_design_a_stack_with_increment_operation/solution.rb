# LeetCode 1381 - Design A Stack With Increment Operation
# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack
  def initialize(max_size)
    @max_size = max_size
    @a = []
  end

  def push(x)
    @a << x if @a.length < @max_size
  end

  def pop
    @a.empty? ? -1 : @a.pop
  end

  def increment(k, val)
    [k, @a.length].min.times { |i| @a[i] += val }
  end
end
