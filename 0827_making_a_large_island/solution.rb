# LeetCode 0827 - Making A Large Island
# https://leetcode.com/problems/making-a-large-island/

# @param {Integer[][]} grid
# @return {Integer}
def largest_island(grid)
  n = grid.length
  sizes = { 0 => 0 }
  island_id = 2

  dfs = lambda do |r, c, iid|
    return 0 if r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1

    grid[r][c] = iid
    1 + dfs.call(r + 1, c, iid) + dfs.call(r - 1, c, iid) +
      dfs.call(r, c + 1, iid) + dfs.call(r, c - 1, iid)
  end

  n.times do |i|
    n.times do |j|
      if grid[i][j] == 1
        sizes[island_id] = dfs.call(i, j, island_id)
        island_id += 1
      end
    end
  end

  ans = sizes.values.max || 0
  n.times do |i|
    n.times do |j|
      next unless grid[i][j] == 0

      seen = {}
      total = 1
      [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]].each do |ni, nj|
        next unless ni >= 0 && ni < n && nj >= 0 && nj < n

        iid = grid[ni][nj]
        if iid > 1 && !seen[iid]
          seen[iid] = true
          total += sizes[iid]
        end
      end
      ans = total if total > ans
    end
  end
  ans
end
