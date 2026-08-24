# LeetCode 0821 - Shortest Distance to a Character
# https://leetcode.com/problems/shortest-distance-to-a-character/

# @param {String} s
# @param {String} c
# @return {Integer[]}
def shortest_to_char(s, c)
  n = s.length
  ans = Array.new(n, 0)
  prev = -n
  s.each_char.with_index do |ch, i|
    prev = i if ch == c
    ans[i] = i - prev
  end
  prev = 2 * n
  (n - 1).downto(0) do |i|
    prev = i if s[i] == c
    ans[i] = [ans[i], prev - i].min
  end
  ans
end
