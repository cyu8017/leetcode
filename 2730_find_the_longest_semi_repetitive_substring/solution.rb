# LeetCode 2730 - Find the Longest Semi-Repetitive Substring
# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

# @param {String} s
# @return {Integer}
def longest_semi_repetitive_substring(s)
  ans = 0
  left = 0
  last_pair = -1
  (0...s.length).each do |right|
    if right > 0 && s[right] == s[right - 1]
      left = last_pair + 1 if last_pair >= left
      last_pair = right - 1
    end
    ans = [ans, right - left + 1].max
  end
  ans
end
