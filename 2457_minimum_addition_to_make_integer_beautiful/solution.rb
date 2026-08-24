# LeetCode 2457 - Minimum Addition to Make Integer Beautiful
# https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

# @param {Integer} n
# @param {Integer} target
# @return {Integer}
def make_integer_beautiful(n, target)
  digit_sum = lambda do |x|
    s = 0
    while x > 0
      s += x % 10
      x /= 10
    end
    s
  end

  orig = n
  pow10 = 1
  while digit_sum.call(n) > target
    n = n / 10 + 1
    pow10 *= 10
  end
  n * pow10 - orig
end
