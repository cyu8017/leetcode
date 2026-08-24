# LeetCode 3964 - Minimum Lights To Illuminate A Road
# https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

# @param {Integer[]} lights
# @return {Integer}
def min_lights(lights)
  n = lights.length
  d = Array.new(n, 0)
  n.times do |i|
    v = lights[i]
    next unless v > 0
    l = [0, i - v].max
    r = [n - 1, i + v].min
    d[l] += 1
    d[r + 1] -= 1 if r + 1 < n
  end
  s = 0
  cnt = 0
  ans = 0
  d.each do |x|
    s += x
    if s == 0
      cnt += 1
    else
      ans += (cnt + 2) / 3
      cnt = 0
    end
  end
  ans += (cnt + 2) / 3
  ans
end
