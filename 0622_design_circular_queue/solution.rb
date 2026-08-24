# LeetCode 0622 - Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue
  def initialize(k)
    @data = Array.new(k, 0)
    @capacity = k
    @head = 0
    @size = 0
  end

  def en_queue(value)
    return false if is_full

    @data[(@head + @size) % @capacity] = value
    @size += 1
    true
  end

  def de_queue
    return false if is_empty

    @head = (@head + 1) % @capacity
    @size -= 1
    true
  end

  def front
    is_empty ? -1 : @data[@head]
  end

  def rear
    return -1 if is_empty

    @data[(@head + @size - 1) % @capacity]
  end

  def is_empty
    @size.zero?
  end

  def is_full
    @size == @capacity
  end
end
