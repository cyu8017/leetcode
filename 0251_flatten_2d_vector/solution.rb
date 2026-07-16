# LeetCode 0251 - Flatten 2D Vector
# https://leetcode.com/problems/flatten-2d-vector/

class Vector2D
  def initialize(vec)
    @vec = vec
    @row = 0
    @col = 0
    advance
  end

  def next
    value = @vec[@row][@col]
    @col += 1
    advance
    value
  end

  def has_next
    advance
    @row < @vec.length
  end

  private

  def advance
    while @row < @vec.length && @col >= @vec[@row].length
      @row += 1
      @col = 0
    end
  end
end
