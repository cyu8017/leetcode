# LeetCode 1414 - Find The Minimum Number Of Fibonacci Numbers Whose Sum Is K
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

def find_min_fibonacci_numbers(k)
  fib = [1, 1]
  fib << fib[-1] + fib[-2] while fib[-1] < k
  answer = 0
  fib.reverse_each do |value|
    if value <= k
      k -= value
      answer += 1
    end
  end
  answer
end
