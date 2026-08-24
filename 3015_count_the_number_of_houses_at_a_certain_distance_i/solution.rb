# LeetCode 3015 - Count the Number of Houses at a Certain Distance I
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

# @param {Integer} n
# @param {Integer} x
# @param {Integer} y
# @return {Integer[]}
def count_of_pairs(n, x, y)
  ans = Array.new(n, 0)
  x -= 1
  y -= 1
  n.times do |i|
    (i + 1...n).each do |j|
      a = j - i
      b = (x - i).abs + (y - j).abs + 1
      c = (x - j).abs + (y - i).abs + 1
      ans[[a, b, c].min - 1] += 2
    end
  end
  ans
end
