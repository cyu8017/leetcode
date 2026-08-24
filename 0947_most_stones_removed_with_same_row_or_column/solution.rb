# LeetCode 0947 - Most Stones Removed with Same Row or Column
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

# @param {Integer[][]} stones
# @return {Integer}
def remove_stones(stones)
  parent = {}

  find = lambda do |x|
    parent[x] = x unless parent.key?(x)
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = ->(a, b) { parent[find.call(a)] = find.call(b) }

  stones.each { |x, y| union.call(x, ~y) }
  roots = {}
  stones.each { |x, _| roots[find.call(x)] = true }
  stones.length - roots.length
end
