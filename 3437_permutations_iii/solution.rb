# LeetCode 3437 - Permutations III
# https://leetcode.com/problems/permutations-iii/

# @param {Integer} n
# @return {Integer[][]}
def permute(n)
  ans = []
  used = Array.new(n + 1, false)
  cur = []
  dfs = nil
  dfs = lambda do
    if cur.length == n
      ans << cur.dup
      return
    end
    (1..n).each do |i|
      next if used[i]
      next if !cur.empty? && (cur[-1] % 2 == i % 2)

      used[i] = true
      cur << i
      dfs.call
      cur.pop
      used[i] = false
    end
  end
  dfs.call
  ans
end
