# LeetCode 3783 - Mirror Distance of an Integer
# https://leetcode.com/problems/mirror-distance-of-an-integer/

# @param {Integer} n
# @return {Integer}
def mirror_distance(n)
  reverse = lambda do |x|
    y = 0
    while x > 0
      y = y * 10 + x % 10
      x /= 10
    end
    y
  end
  (n - reverse.call(n)).abs
end
