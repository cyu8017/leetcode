# LeetCode 3470 - Permutations IV
# https://leetcode.com/problems/permutations-iv/

# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def permute(n, k)
  fact = Array.new(n + 1, 0)
  fact[0] = 1
  (1..n).each do |i|
    fact[i] = fact[i - 1] * i
    fact[i] = 10**18 + 1 if fact[i] > 10**18
  end
  used = Array.new(n + 1, false)
  ans = []
  kk = k
  dfs = nil
  dfs = lambda do |pos|
    return true if pos == n

    (1..n).each do |x|
      next if used[x]
      next if pos > 0 && (ans[pos - 1] % 2 == x % 2)

      rem = n - pos - 1
      cnt = fact[rem]
      if cnt >= kk
        used[x] = true
        ans << x
        return true if dfs.call(pos + 1)

        ans.pop
        used[x] = false
      else
        kk -= cnt
      end
    end
    false
  end
  return [] unless dfs.call(0)

  ans
end
