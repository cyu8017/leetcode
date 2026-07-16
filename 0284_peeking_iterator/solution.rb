# LeetCode 0284 - Peeking Iterator
# https://leetcode.com/problems/peeking-iterator/

class ListIterator
  def initialize(values)
    @values = values
    @index = 0
  end

  def next
    value = @values[@index]
    @index += 1
    value
  end

  def hasNext
    @index < @values.length
  end
end

class PeekingIterator
  def initialize(iterator)
    @iterator = iterator
    @peeked = nil
    @has_peeked = false
  end

  def peek
    unless @has_peeked
      @peeked = @iterator.next
      @has_peeked = true
    end
    @peeked
  end

  def next
    if @has_peeked
      result = @peeked
      @peeked = nil
      @has_peeked = false
      return result
    end
    @iterator.next
  end

  def hasNext
    @has_peeked || @iterator.hasNext
  end
end
