# LeetCode 3773 - Maximum Number of Equal Length Runs
# https://leetcode.com/problems/maximum-number-of-equal-length-runs/

# @param {String} s
# @return {Integer}
def max_same_length_runs(s)
  cnt = Hash.new(0)
  n = s.length
  ans = 0
  i = 0
  while i < n
    j = i + 1
    j += 1 while j < n && s[j] == s[i]
    m = j - i
    cnt[m] += 1
    ans = [ans, cnt[m]].max
    i = j
  end
  ans
end
