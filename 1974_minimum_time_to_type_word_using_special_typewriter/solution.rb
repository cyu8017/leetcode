# LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

# @param {String} word
# @return {Integer}
def min_time_to_type(word)
  cur = "a"
  ans = 0
  word.each_char do |ch|
    d = (ch.ord - cur.ord).abs
    ans += [d, 26 - d].min + 1
    cur = ch
  end
  ans
end
