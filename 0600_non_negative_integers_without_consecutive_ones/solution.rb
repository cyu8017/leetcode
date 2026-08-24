# LeetCode 0600 - Non-negative Integers without Consecutive Ones
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

# @param {Integer} n
# @return {Integer}
def find_integers(n)
  fib = Array.new(32, 0)
  fib[0] = 1
  fib[1] = 2
  (2...32).each { |i| fib[i] = fib[i - 1] + fib[i - 2] }

  answer = 0
  prev_bit = 0
  30.downto(0) do |bit|
    if n & (1 << bit) != 0
      answer += fib[bit]
      return answer if prev_bit == 1

      prev_bit = 1
    else
      prev_bit = 0
    end
  end

  answer + 1
end
