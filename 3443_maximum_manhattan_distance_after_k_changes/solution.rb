# LeetCode 3443 - Maximum Manhattan Distance After K Changes
# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_distance(s, k)
  ans = 0
  lat = 0
  lon = 0
  s.each_char.with_index do |c, i|
    case c
    when "N" then lat += 1
    when "S" then lat -= 1
    when "E" then lon += 1
    else lon -= 1
    end
    md = lat.abs + lon.abs
    steps = i + 1
    cur = md + 2 * k
    cur = steps if cur > steps
    ans = cur if cur > ans
  end
  ans
end
