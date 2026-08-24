# LeetCode 0903 - Valid Permutations for DI Sequence
# https://leetcode.com/problems/valid-permutations-for-di-sequence/

# @param {String} s
# @return {Integer}
def num_perms_di_sequence(s)
  mod = 10**9 + 7
  n = s.length
  dp = Array.new(n + 1, 1)
  (1..n).each do |i|
    new_dp = Array.new(n + 1, 0)
    if s[i - 1] == "I"
      postfix = 0
      (n - i).downto(0) do |j|
        postfix = (postfix + dp[j + 1]) % mod
        new_dp[j] = postfix
      end
    else
      prefix = 0
      (0..(n - i)).each do |j|
        prefix = (prefix + dp[j]) % mod
        new_dp[j] = prefix
      end
    end
    dp = new_dp
  end
  dp[0]
end
