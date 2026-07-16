# LeetCode 0281 - Zigzag Iterator
# https://leetcode.com/problems/zigzag-iterator/

class ZigzagIterator
  def initialize(v1, v2)
    @vectors = [v1, v2]
    @indices = [0, 0]
    @turn = 0
  end

  def next
    while @indices[@turn] >= @vectors[@turn].length
      @turn = 1 - @turn
    end
    value = @vectors[@turn][@indices[@turn]]
    @indices[@turn] += 1
    @turn = 1 - @turn
    value
  end

  def hasNext
    @indices.each_with_index.any? { |index, vector_index| index < @vectors[vector_index].length }
  end
end
