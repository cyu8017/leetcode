# LeetCode 1114 - Print in Order
# https://leetcode.com/problems/print-in-order/

class Foo
  def initialize
    @second_ready = false
    @third_ready = false
    @mutex = Mutex.new
    @cv = ConditionVariable.new
  end

  def first(print_first)
    print_first.call
    @mutex.synchronize do
      @second_ready = true
      @cv.broadcast
    end
  end

  def second(print_second)
    @mutex.synchronize do
      @cv.wait(@mutex) until @second_ready
    end
    print_second.call
    @mutex.synchronize do
      @third_ready = true
      @cv.broadcast
    end
  end

  def third(print_third)
    @mutex.synchronize do
      @cv.wait(@mutex) until @third_ready
    end
    print_third.call
  end
end
