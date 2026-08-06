# LeetCode 1115 - Print FooBar Alternately
# https://leetcode.com/problems/print-foobar-alternately/

class FooBar
  def initialize(n)
    @n = n
    @foo_turn = true
    @mutex = Mutex.new
    @cv = ConditionVariable.new
  end

  def foo(print_foo)
    @n.times do
      @mutex.synchronize do
        @cv.wait(@mutex) until @foo_turn
        print_foo.call
        @foo_turn = false
        @cv.broadcast
      end
    end
  end

  def bar(print_bar)
    @n.times do
      @mutex.synchronize do
        @cv.wait(@mutex) until !@foo_turn
        print_bar.call
        @foo_turn = true
        @cv.broadcast
      end
    end
  end
end
