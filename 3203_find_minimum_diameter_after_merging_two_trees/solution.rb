# LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

# @param {Integer[][]} edges1
# @param {Integer[][]} edges2
# @return {Integer}
def minimum_diameter_after_merge(edges1, edges2)
  state = { ans: 0, a: 0, g: [] }
  dfs = lambda do |i, fa, t|
    state[:g][i].each do |j|
      dfs.call(j, i, t + 1) if j != fa
    end
    if state[:ans] < t
      state[:ans] = t
      state[:a] = i
    end
  end
  tree_diameter = lambda do |edges|
    nn = edges.length + 1
    state[:g] = Array.new(nn) { [] }
    edges.each do |e|
      state[:g][e[0]] << e[1]
      state[:g][e[1]] << e[0]
    end
    state[:ans] = 0
    state[:a] = 0
    dfs.call(0, -1, 0)
    dfs.call(state[:a], -1, 0)
    state[:ans]
  end
  d1 = tree_diameter.call(edges1)
  d2 = tree_diameter.call(edges2)
  [d1, d2, (d1 + 1) / 2 + (d2 + 1) / 2 + 1].max
end
