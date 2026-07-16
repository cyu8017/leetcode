# LeetCode 0225 - Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack
  def initialize
    @queue = []
  end

  # @param {Integer} x
  # @return {Void}
  def push(x)
    @queue.push(x)
    (@queue.length - 1).times { @queue.push(@queue.shift) }
    nil
  end

  # @return {Integer}
  def pop
    @queue.shift
  end

  # @return {Integer}
  def top
    @queue[0]
  end

  # @return {Boolean}
  def empty
    @queue.empty?
  end
end
