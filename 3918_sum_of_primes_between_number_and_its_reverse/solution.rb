# LeetCode 3918 - Sum of Primes Between Number and Its Reverse
# https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

$is_prime3918 = nil

def init3918
  return unless $is_prime3918.nil?
  $is_prime3918 = Array.new(1001, true)
  $is_prime3918[0] = $is_prime3918[1] = false
  i = 2
  while i * i <= 1000
    if $is_prime3918[i]
      j = i * i
      while j <= 1000
        $is_prime3918[j] = false
        j += i
      end
    end
    i += 1
  end
end

# @param {Integer} n
# @return {Integer}
def sum_of_primes_in_range(n)
  init3918
  r = 0
  x = n
  while x > 0
    r = r * 10 + x % 10
    x /= 10
  end
  low = [n, r].min
  high = [n, r].max
  ans = 0
  (low..high).each { |v| ans += v if $is_prime3918[v] }
  ans
end
