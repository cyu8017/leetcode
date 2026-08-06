# LeetCode 1286 - Iterator for Combination
# https://leetcode.com/problems/iterator-for-combination/

class CombinationIterator
  def initialize(characters, combination_length)
    @items = characters.chars.combination(combination_length).map(&:join)
    @index = 0
  end

  def next
    value = @items[@index]
    @index += 1
    value
  end

  def has_next
    @index < @items.length
  end
end
