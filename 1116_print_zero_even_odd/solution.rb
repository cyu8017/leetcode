# LeetCode 1116 - Print Zero Even Odd
# https://leetcode.com/problems/print-zero-even-odd/

class ZeroEvenOdd
  def initialize(n)
    @n = n
    @state = :zero
    @num = 1
    @mutex = Mutex.new
    @cv = ConditionVariable.new
  end

  def zero(print_number)
    @n.times do
      @mutex.synchronize do
        @cv.wait(@mutex) until @state == :zero
        print_number.call(0)
        @state = (@num.odd? ? :odd : :even)
        @cv.broadcast
      end
    end
  end

  def even(print_number)
    (@n / 2).times do
      @mutex.synchronize do
        @cv.wait(@mutex) until @state == :even
        print_number.call(@num)
        @num += 1
        @state = :zero
        @cv.broadcast
      end
    end
  end

  def odd(print_number)
    ((@n + 1) / 2).times do
      @mutex.synchronize do
        @cv.wait(@mutex) until @state == :odd
        print_number.call(@num)
        @num += 1
        @state = :zero
        @cv.broadcast
      end
    end
  end
end
