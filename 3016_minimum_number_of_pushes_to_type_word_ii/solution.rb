# LeetCode 3016 - Minimum Number of Pushes to Type Word II
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

# @param {String} word
# @return {Integer}
def minimum_pushes(word)
  cnt = Array.new(26, 0)
  word.each_char { |ch| cnt[ch.ord - 97] += 1 }
  cnt.sort!
  ans = 0
  26.times { |i| ans += (i / 8 + 1) * cnt[26 - i - 1] }
  ans
end
