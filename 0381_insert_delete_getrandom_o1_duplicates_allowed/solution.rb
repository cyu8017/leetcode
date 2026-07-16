# LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

require "set"

class RandomizedCollection
  def initialize
    @values = []
    @indices = {}
  end

  def insert(val)
    @indices[val] ||= Set.new
    @indices[val].add(@values.length)
    @values << val
    @indices[val].length == 1
  end

  def remove(val)
    return false unless @indices[val]&.any?

    index = @indices[val].first
    last_index = @values.length - 1
    last_value = @values[last_index]
    @values[index] = last_value
    @indices[last_value].delete(last_index)
    @indices[last_value].add(index)
    @values.pop
    @indices[val].delete(index)
    @indices.delete(val) if @indices[val].empty?
    true
  end

  def get_random
    @values.last
  end

  alias_method :getRandom, :get_random
end
