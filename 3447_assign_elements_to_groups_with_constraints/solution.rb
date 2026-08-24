# LeetCode 3447 - Assign Elements to Groups with Constraints
# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

# @param {Integer[]} groups
# @param {Integer[]} elements
# @return {Integer[]}
def assign_elements(groups, elements)
  max_v = 100_001
  first = Array.new(max_v, -1)
  elements.each_with_index do |e, i|
    first[e] = i if e < max_v && first[e] == -1
  end
  ans = Array.new(groups.length, 0)
  groups.each_with_index do |g, gi|
    best = -1
    d = 1
    while d * d <= g
      if g % d == 0
        best = first[d] if first[d] != -1 && (best == -1 || first[d] < best)
        other = g / d
        best = first[other] if first[other] != -1 && (best == -1 || first[other] < best)
      end
      d += 1
    end
    ans[gi] = best
  end
  ans
end
