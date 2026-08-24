# LeetCode 0641 - Design Circular Deque
# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque
  def initialize(k)
    @data = Array.new(k, 0)
    @capacity = k
    @front = 0
    @size = 0
  end

  def insert_front(value)
    return false if is_full

    @front = (@front - 1) % @capacity
    @data[@front] = value
    @size += 1
    true
  end

  def insert_last(value)
    return false if is_full

    @data[(@front + @size) % @capacity] = value
    @size += 1
    true
  end

  def delete_front
    return false if is_empty

    @front = (@front + 1) % @capacity
    @size -= 1
    true
  end

  def delete_last
    return false if is_empty

    @size -= 1
    true
  end

  def get_front
    is_empty ? -1 : @data[@front]
  end

  def get_rear
    return -1 if is_empty

    @data[(@front + @size - 1) % @capacity]
  end

  def is_empty
    @size.zero?
  end

  def is_full
    @size == @capacity
  end
end
