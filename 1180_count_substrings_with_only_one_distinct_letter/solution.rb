# LeetCode 1180 - Count Substrings with Only One Distinct Letter
# https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

# @param {String} s
# @return {Integer}
def count_letters(s)
  ans = length = 1
  (1...s.length).each do |i|
    length = s[i] == s[i - 1] ? length + 1 : 1
    ans += length
  end
  ans
end
