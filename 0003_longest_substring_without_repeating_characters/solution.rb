# LeetCode 0003 - Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  last = {}
  best = 0
  start = 0

  s.each_char.with_index do |ch, i|
    if last.key?(ch) && last[ch] >= start
      start = last[ch] + 1
    end
    last[ch] = i
    best = [best, i - start + 1].max
  end

  best
end
