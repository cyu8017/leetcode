# LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

# @param {Integer} n
# @return {String}
def concat_hex36(n)
  f = lambda do |x, k|
    res = []
    while x > 0
      v = x % k
      res << (v <= 9 ? (48 + v).chr : (65 + v - 10).chr)
      x /= k
    end
    res.reverse.join
  end
  f.call(n * n, 16) + f.call(n * n * n, 36)
end
