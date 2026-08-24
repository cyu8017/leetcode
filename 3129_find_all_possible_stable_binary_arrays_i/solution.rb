# LeetCode 3129 - Find All Possible Stable Binary Arrays I
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

# @param {Integer} zero
# @param {Integer} one
# @param {Integer} limit
# @return {Integer}
def number_of_stable_arrays(zero, one, limit)
  mod = 1_000_000_007
  f = Array.new(zero + 1) { Array.new(one + 1) { [-1, -1] } }

  dfs = lambda do |i, j, k|
    return 0 if i < 0 || j < 0
    return (k == 1 && j <= limit) ? 1 : 0 if i == 0
    return (k == 0 && i <= limit) ? 1 : 0 if j == 0
    return f[i][j][k] if f[i][j][k] != -1
    res = if k == 0
            (dfs.call(i - 1, j, 0) + dfs.call(i - 1, j, 1) - dfs.call(i - limit - 1, j, 1) + mod) % mod
          else
            (dfs.call(i, j - 1, 0) + dfs.call(i, j - 1, 1) - dfs.call(i, j - limit - 1, 0) + mod) % mod
          end
    f[i][j][k] = res
    res
  end

  (dfs.call(zero, one, 0) + dfs.call(zero, one, 1)) % mod
end
