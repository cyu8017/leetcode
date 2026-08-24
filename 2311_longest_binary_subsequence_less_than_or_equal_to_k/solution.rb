# LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def longest_subsequence(s, k)
  zeros = s.count("0")
  val = 0
  ones = 0
  pow2 = 1
  (s.length - 1).downto(0) do |i|
    if s[i] == "1"
      unless pow2 > k || val + pow2 > k
        val += pow2
        ones += 1
      end
    end
    pow2 *= 2 if pow2 <= k
  end
  zeros + ones
end
