# LeetCode 1172 - Dinner Plate Stacks
# https://leetcode.com/problems/dinner-plate-stacks/

class DinnerPlates
  def initialize(capacity)
    @capacity = capacity
    @stacks = []
    @available = []
  end

  def push(val)
    while !@available.empty? && (@available[0] >= @stacks.length || @stacks[@available[0]].length == @capacity)
      @available.shift
    end
    if @available.empty?
      @stacks << []
      insert_avail(@stacks.length - 1)
    end
    idx = @available[0]
    @stacks[idx] << val
    @available.shift if @stacks[idx].length == @capacity
  end

  def pop
    @stacks.pop while !@stacks.empty? && @stacks[-1].empty?
    @stacks.empty? ? -1 : pop_at_stack(@stacks.length - 1)
  end

  def pop_at_stack(index)
    return -1 if index < 0 || index >= @stacks.length || @stacks[index].empty?
    insert_avail(index) if @stacks[index].length == @capacity
    @stacks[index].pop
  end

  private

  def insert_avail(idx)
    return if @available.include?(idx)
    pos = @available.bsearch_index { |x| x >= idx } || @available.length
    @available.insert(pos, idx)
  end
end
