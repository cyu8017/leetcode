# LeetCode 3133 - Minimum Array End
# https://leetcode.com/problems/minimum-array-end/

# @param {Integer} n
# @param {Integer} x
# @return {Integer}
def min_end(n, x)
  n -= 1
  ans = x
  31.times do |i|
    if ((x >> i) & 1) == 0
      ans |= (n & 1) << i
      n >>= 1
    end
  end
  ans |= n << 31
  ans
end
