# LeetCode 1206 - Design Skiplist
# https://leetcode.com/problems/design-skiplist/

class Skiplist
  def initialize
    @values = []
  end

  def search(target)
    i = @values.bsearch_index { |x| x >= target } || @values.length
    i < @values.length && @values[i] == target
  end

  def add(num)
    i = @values.bsearch_index { |x| x >= num } || @values.length
    @values.insert(i, num)
  end

  def erase(num)
    i = @values.bsearch_index { |x| x >= num } || @values.length
    return false if i == @values.length || @values[i] != num
    @values.delete_at(i)
    true
  end
end
