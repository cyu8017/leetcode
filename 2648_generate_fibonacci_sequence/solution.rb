# LeetCode 2648 - Generate Fibonacci Sequence
# https://leetcode.com/problems/generate-fibonacci-sequence/

# @return {Enumerator}
def fib_generator
  Enumerator.new do |y|
    a = 0
    b = 1
    loop do
      y << a
      a, b = b, a + b
    end
  end
end

def solve(*args)
  fib_generator(*args)
end
