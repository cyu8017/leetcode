# LeetCode 0519 - Random Flip Matrix
# https://leetcode.com/problems/random-flip-matrix/

$uniform = nil

def set_uniform(fn)
  $uniform = fn
end

class Solution
  def initialize(m, n)
    @rows = m
    @cols = n
    @total = m * n
    reset
  end

  def flip
    index = $uniform.call(0, @available.length - 1).to_i
    index = @available.length - 1 if index >= @available.length
    value = @available[index]
    @available[index] = @available[-1]
    @available.pop
    [value / @cols, value % @cols]
  end

  def reset
    @available = (0...@total).to_a
  end
end
