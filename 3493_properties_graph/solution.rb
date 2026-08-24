# LeetCode 3493 - Properties Graph
# https://leetcode.com/problems/properties-graph/

# @param {Integer[][]} properties
# @param {Integer} k
# @return {Integer}
def number_of_components(properties, k)
  n = properties.length
  sets = properties.map { |row| row.each_with_object({}) { |v, h| h[v] = true } }
  parent = (0...n).to_a
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb if ra != rb
  end
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      cnt = 0
      sets[i].each_key { |v| cnt += 1 if sets[j][v] }
      unite.call(i, j) if cnt >= k
    end
  end
  comp = {}
  (0...n).each { |i| comp[find.call(i)] = true }
  comp.length
end
