# LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
# https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

# @param {String} s
# @return {Integer}
def minimum_time(s)
  n = s.length
  left = Array.new(n, 0)
  left[0] = 1 if s[0] == "1"
  (1...n).each do |i|
    left[i] = left[i - 1]
    left[i] = [i + 1, left[i - 1] + 2].min if s[i] == "1"
  end
  ans = left[n - 1]
  right = 0
  (n - 1).downto(0) do |i|
    right = [n - i, right + 2].min if s[i] == "1"
    left_cost = i > 0 ? left[i - 1] : 0
    ans = [ans, left_cost + right].min
  end
  ans
end
