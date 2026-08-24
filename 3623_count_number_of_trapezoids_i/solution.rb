# LeetCode 3623 - Count Number of Trapezoids I
# https://leetcode.com/problems/count-number-of-trapezoids-i/

# @param {Integer[][]} points
# @return {Integer}
def count_trapezoids(points)
  mod = 1_000_000_007
  cnt = Hash.new(0)
  points.each { |p| cnt[p[1]] += 1 }
  ans = 0
  pre = 0
  cnt.each_value do |c|
    lines = c * (c - 1) / 2
    ans = (ans + pre * lines) % mod
    pre = (pre + lines) % mod
  end
  ans
end
