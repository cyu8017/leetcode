# LeetCode 0940 - Distinct Subsequences II
# https://leetcode.com/problems/distinct-subsequences-ii/

# @param {String} s
# @return {Integer}
def distinct_subseq_ii(s)
  mod = 10**9 + 7
  ends = Hash.new(0)
  ends[""] = 1
  s.each_char do |ch|
    ends[ch] = ends.values.sum % mod
  end
  (ends.values.sum - 1) % mod
end
