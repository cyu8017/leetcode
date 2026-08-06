# LeetCode 1188 - Design Bounded Blocking Queue
# https://leetcode.com/problems/design-bounded-blocking-queue/

class BoundedBlockingQueue
  def initialize(capacity)
    @capacity = capacity
    @queue = []
    @mutex = Mutex.new
    @not_full = ConditionVariable.new
    @not_empty = ConditionVariable.new
  end

  def enqueue(element)
    @mutex.synchronize do
      @not_full.wait(@mutex) while @queue.length == @capacity
      @queue << element
      @not_empty.signal
    end
  end

  def dequeue
    @mutex.synchronize do
      @not_empty.wait(@mutex) while @queue.empty?
      value = @queue.shift
      @not_full.signal
      value
    end
  end

  def size
    @mutex.synchronize { @queue.length }
  end
end
