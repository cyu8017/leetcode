# LeetCode 3556 - Sum of Largest Prime Substrings
# https://leetcode.com/problems/sum-of-largest-prime-substrings/

# @param {String} s
# @return {Integer}
def sum_of_largest_primes(s)
  is_prime = lambda do |x|
    return false if x < 2
    sqrt_x = Math.sqrt(x).to_i
    (2..sqrt_x).each { |i| return false if x % i == 0 }
    true
  end
  st = {}
  n = s.length
  (0...n).each do |i|
    x = 0
    (i...n).each do |j|
      x = x * 10 + (s[j].ord - 48)
      st[x] = true if is_prime.call(x)
    end
  end
  nums = st.keys.sort
  ans = 0
  i = nums.length - 1
  while i >= 0 && nums.length - i <= 3
    ans += nums[i]
    i -= 1
  end
  ans
end
