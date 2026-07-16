# LeetCode 0313 - Super Ugly Number
# https://leetcode.com/problems/super-ugly-number/

class Solution
  def nthSuperUglyNumber(n, primes)
    ugly = [1]
    pointers = Array.new(primes.length, 0)
    while ugly.length < n
      next_values = primes.each_with_index.map { |prime, index| ugly[pointers[index]] * prime }
      next_ugly = next_values.min
      ugly << next_ugly
      primes.each_with_index do |prime, index|
        pointers[index] += 1 if next_ugly == ugly[pointers[index]] * prime
      end
    end
    ugly[-1]
  end
end
