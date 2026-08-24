# LeetCode 3959 - Check Good Integer
# https://leetcode.com/problems/check-good-integer/

# @param {Integer} n
# @return {Boolean}
def check_good_integer(n)
  s = 0
  while n > 0
    x = n % 10
    s += x * (x - 1)
    n /= 10
  end
  s >= 50
end
