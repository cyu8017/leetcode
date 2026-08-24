# LeetCode 0753 - Cracking the Safe
# https://leetcode.com/problems/cracking-the-safe/

# @param {Integer} n
# @param {Integer} k
# @return {String}
def crack_safe(n, k)
  seen = {}
  path = []
  start = "0" * [n - 1, 0].max

  dfs = lambda do |node|
    k.times do |digit|
      edge = node + digit.to_s
      next if seen[edge]

      seen[edge] = true
      dfs.call(edge[1..] || "")
      path << digit.to_s
    end
  end

  dfs.call(start)
  path.join + start
end
