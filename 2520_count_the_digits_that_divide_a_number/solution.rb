# LeetCode 2520 - Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

# @param {Integer} num
# @return {Integer}
def count_digits(num)
  ans = 0
  x = num
  while x > 0
    d = x % 10
    ans += 1 if d != 0 && num % d == 0
    x /= 10
  end
  ans
end
