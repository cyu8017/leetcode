# LeetCode 0202 - Happy Number
# https://leetcode.com/problems/happy-number/

# @param {Integer} n
# @return {Boolean}
def is_happy(n)
  seen = {}
  while n != 1 && !seen[n]
    seen[n] = true
    total = 0
    while n > 0
      digit = n % 10
      total += digit * digit
      n /= 10
    end
    n = total
  end
  n == 1
end