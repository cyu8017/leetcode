# LeetCode 3531 - Count Covered Buildings
# https://leetcode.com/problems/count-covered-buildings/

# @param {Integer} n
# @param {Integer[][]} buildings
# @return {Integer}
def count_covered_buildings(n, buildings)
  g1 = {}
  g2 = {}
  buildings.each do |b|
    (g1[b[0]] ||= []) << b[1]
    (g2[b[1]] ||= []) << b[0]
  end
  g1.each_value(&:sort!)
  g2.each_value(&:sort!)
  ans = 0
  buildings.each do |b|
    x, y = b[0], b[1]
    l1 = g1[x]
    l2 = g2[y]
    ans += 1 if l2[0] < x && x < l2[-1] && l1[0] < y && y < l1[-1]
  end
  ans
end
