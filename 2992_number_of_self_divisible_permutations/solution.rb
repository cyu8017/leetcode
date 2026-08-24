# LeetCode 2992 - Number of Self-Divisible Permutations
# https://leetcode.com/problems/number-of-self-divisible-permutations/

# @param {Integer} n
# @return {Integer}
def self_divisible_permutation_count(n)
  ans = 0
  used = Array.new(n + 1, false)
  dfs = lambda do |pos|
    if pos > n
      ans += 1
      return
    end
    (1..n).each do |v|
      next if used[v]
      next if v.gcd(pos) != 1

      used[v] = true
      dfs.call(pos + 1)
      used[v] = false
    end
  end
  dfs.call(1)
  ans
end

def solve(*args)
  self_divisible_permutation_count(*args)
end
