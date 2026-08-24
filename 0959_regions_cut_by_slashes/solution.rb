# LeetCode 0959 - Regions Cut By Slashes
# https://leetcode.com/problems/regions-cut-by-slashes/

# @param {String[]} grid
# @return {Integer}
def regions_by_slashes(grid)
  n = grid.length
  parent = (0...(n * n * 4)).to_a

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = ->(a, b) { parent[find.call(a)] = find.call(b) }

  n.times do |r|
    n.times do |c|
      root = 4 * (r * n + c)
      ch = grid[r][c]
      if ch == "/"
        union.call(root + 0, root + 3)
        union.call(root + 1, root + 2)
      elsif ch == "\\"
        union.call(root + 0, root + 1)
        union.call(root + 2, root + 3)
      else
        union.call(root + 0, root + 1)
        union.call(root + 1, root + 2)
        union.call(root + 2, root + 3)
      end
      union.call(root + 2, root + 4 * n + 0) if r + 1 < n
      union.call(root + 1, root + 4 + 3) if c + 1 < n
    end
  end

  (0...(n * n * 4)).count { |i| find.call(i) == i }
end
