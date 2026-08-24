# LeetCode 0716 - Max Stack
# https://leetcode.com/problems/max-stack/

class MaxStack
  def initialize
    @stack = []
    @maxes = []
  end

  def push(x)
    @stack << x
    @maxes << (@maxes.empty? ? x : [x, @maxes[-1]].max)
    nil
  end

  def pop
    @maxes.pop
    @stack.pop
  end

  def top
    @stack[-1]
  end

  def peek_max
    @maxes[-1]
  end

  def pop_max
    max_val = peek_max
    buffer = []
    buffer << pop while top != max_val
    pop
    push(buffer.pop) until buffer.empty?
    max_val
  end
end
