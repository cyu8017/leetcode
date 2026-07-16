# LeetCode 0380 - Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet
  def initialize
    @values = []
    @index_by_value = {}
  end

  def insert(val)
    return false if @index_by_value.key?(val)

    @index_by_value[val] = @values.length
    @values << val
    true
  end

  def remove(val)
    return false unless @index_by_value.key?(val)

    index = @index_by_value[val]
    last_value = @values[-1]
    @values[index] = last_value
    @index_by_value[last_value] = index
    @values.pop
    @index_by_value.delete(val)
    true
  end

  def get_random
    @values.sample
  end

  alias_method :getRandom, :get_random
end
