# LeetCode 0232 - Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue
  def initialize
    @input_stack = []
    @output_stack = []
  end

  # @param {Integer} x
  # @return {Void}
  def push(x)
    @input_stack.push(x)
    nil
  end

  # @return {Integer}
  def pop
    move
    @output_stack.pop
  end

  # @return {Integer}
  def peek
    move
    @output_stack.last
  end

  # @return {Boolean}
  def empty
    @input_stack.empty? && @output_stack.empty?
  end

  private

  def move
    return unless @output_stack.empty?

    @output_stack.push(@input_stack.pop) until @input_stack.empty?
  end
end
