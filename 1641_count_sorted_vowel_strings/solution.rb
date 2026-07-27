# LeetCode 1641 - Count Sorted Vowel Strings
# https://leetcode.com/problems/count-sorted-vowel-strings/

def _comb_1641(n, k)
  return 0 if k < 0 || k > n
  return 1 if k.zero? || k == n

  k = n - k if k > n - k
  res = 1
  (1..k).each { |i| res = res * (n - k + i) / i }
  res
end

# @param {Integer} n
# @return {Integer}
def count_vowel_strings(n)
  _comb_1641(n + 4, 4)
end
