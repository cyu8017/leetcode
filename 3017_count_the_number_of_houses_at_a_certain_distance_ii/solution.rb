# LeetCode 3017 - Count the Number of Houses at a Certain Distance II
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

# @param {Integer} n
# @param {Integer} x
# @param {Integer} y
# @return {Integer[]}
def count_of_pairs(n, x, y)
  x, y = y, x if x > y
  a = Array.new(n, 0)
  (1..n).each do |i|
    a[0] += 2
    a[[i - 1, (i - y).abs + x].min] -= 1
    a[[n - i, (i - x).abs + 1 + (n - y)].min] -= 1
    a[[(i - x).abs, (y - i).abs + 1].min] += 1
    a[[(i - x).abs + 1, (y - i).abs].min] += 1
    r = [x - i, 0].max + [i - y, 0].max
    a[r + ((y - x) / 2)] -= 1
    a[r + ((y - x + 1) / 2)] -= 1
  end
  (1...n).each { |i| a[i] += a[i - 1] }
  a
end
