# LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
# https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

# @param {Integer} k
# @return {Integer}
def ways_to_reach_stair(k)
  f = {}

  dfs = lambda do |i, j, jump|
    return 0 if i > k + 1
    key = [i, j, jump]
    return f[key] if f.key?(key)
    ans = 0
    ans += 1 if i == k
    ans += dfs.call(i - 1, 1, jump) if i > 0 && j == 0
    ans += dfs.call(i + (1 << jump), 0, jump + 1)
    f[key] = ans
    ans
  end

  dfs.call(1, 0, 0)
end
