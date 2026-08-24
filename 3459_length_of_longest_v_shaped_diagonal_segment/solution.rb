# LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

# @param {Integer[][]} grid
# @return {Integer}
def len_of_v_diagonal(grid)
  m = grid.length
  n = grid[0].length
  dirs = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
  next_dir = [1, 2, 3, 0]
  memo = {}
  key_fn = lambda do |i, j, d, turned, expect|
    ((((i * 101 + j) * 5 + d) * 3 + turned) * 5 + expect)
  end
  dfs = nil
  dfs = lambda do |i, j, d, turned, expect|
    return 0 if i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != expect

    k = key_fn.call(i, j, d, turned, expect)
    return memo[k] if memo.key?(k)

    ni = i + dirs[d][0]
    nj = j + dirs[d][1]
    nx = expect == 2 ? 0 : 2
    best = 1 + dfs.call(ni, nj, d, turned, nx)
    if turned == 0
      nd = next_dir[d]
      ti = i + dirs[nd][0]
      tj = j + dirs[nd][1]
      cand = 1 + dfs.call(ti, tj, nd, 1, nx)
      best = cand if cand > best
    end
    memo[k] = best
    best
  end
  ans = 0
  (0...m).each do |i|
    (0...n).each do |j|
      next if grid[i][j] != 1

      (0...4).each do |d|
        ni = i + dirs[d][0]
        nj = j + dirs[d][1]
        best = 1 + dfs.call(ni, nj, d, 0, 2)
        ans = best if best > ans
      end
      ans = 1 if ans < 1
    end
  end
  ans
end
