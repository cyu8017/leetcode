# LeetCode 2761 - Prime Pairs With Target Sum
# https://leetcode.com/problems/prime-pairs-with-target-sum/

# @param {Integer} n
# @return {Integer[][]}
def find_prime_pairs(n)
  is_prime = Array.new(n + 1, true)
  is_prime[0] = is_prime[1] = false
  i = 2
  while i * i <= n
    if is_prime[i]
      (i * i).step(n, i) { |j| is_prime[j] = false }
    end
    i += 1
  end
  ans = []
  (2..(n / 2)).each do |x|
    y = n - x
    ans << [x, y] if is_prime[x] && is_prime[y]
  end
  ans
end
