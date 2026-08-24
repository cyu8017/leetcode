# LeetCode 3009 - Maximum Number of Intersections on the Chart
# https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

# @param {Integer[]} y
# @return {Integer}
def max_intersection_count(y)
  n = y.length
  line = Hash.new(0)
  (1...n).each do |i|
    start = 2 * y[i - 1]
    finish = 2 * y[i]
    unless i == n - 1
      if y[i] > y[i - 1]
        finish -= 1
      else
        finish += 1
      end
    end
    a = start
    b = finish
    a, b = b, a if a > b
    line[a] += 1
    line[b + 1] -= 1
  end
  keys = line.keys.sort
  ans = 0
  cur = 0
  keys.each do |key|
    cur += line[key]
    ans = cur if cur > ans
  end
  ans
end

def solve(*args)
  max_intersection_count(*args)
end
