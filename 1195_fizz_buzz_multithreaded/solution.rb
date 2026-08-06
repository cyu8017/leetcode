# LeetCode 1195 - Fizz Buzz Multithreaded
# https://leetcode.com/problems/fizz-buzz-multithreaded/

class FizzBuzz
  def initialize(n)
    @n = n
    @current = 1
    @mutex = Mutex.new
    @cv = ConditionVariable.new
  end

  def fizz(print_fizz)
    run(->(x) { x % 3 == 0 && x % 5 != 0 }, -> { print_fizz.call })
  end

  def buzz(print_buzz)
    run(->(x) { x % 5 == 0 && x % 3 != 0 }, -> { print_buzz.call })
  end

  def fizzbuzz(print_fizz_buzz)
    run(->(x) { x % 15 == 0 }, -> { print_fizz_buzz.call })
  end

  def number(print_number)
    run(->(x) { x % 3 != 0 && x % 5 != 0 }, -> { print_number.call(@current) })
  end

  private

  def run(predicate, action)
    @mutex.synchronize do
      while @current <= @n
        if predicate.call(@current)
          action.call
          @current += 1
          @cv.broadcast
        else
          @cv.wait(@mutex)
        end
      end
    end
  end
end
