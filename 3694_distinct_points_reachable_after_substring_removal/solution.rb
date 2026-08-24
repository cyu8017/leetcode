# LeetCode 3694 - Distinct Points Reachable After Substring Removal
# https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def distinct_points(s, k)
  n = s.length
  f = Array.new(n + 1, 0)
  g = Array.new(n + 1, 0)
  x = 0
  y = 0
  (1..n).each do |i|
    c = s[i - 1]
    if c == "U"
      y += 1
    elsif c == "D"
      y -= 1
    elsif c == "L"
      x -= 1
    else
      x += 1
    end
    f[i] = x
    g[i] = y
  end
  st = {}
  (k..n).each do |i|
    a = f[n] - (f[i] - f[i - k])
    b = g[n] - (g[i] - g[i - k])
    st[[a, b]] = true
  end
  st.length
end
