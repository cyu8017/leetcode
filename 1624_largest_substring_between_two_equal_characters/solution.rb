# LeetCode 1624 - Largest Substring Between Two Equal Characters
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

# @param {String} s
# @return {Integer}
def max_length_between_equal_characters(s)
  first = {}
  ans = -1
  s.each_char.with_index do |ch, i|
    if first.key?(ch)
      ans = [ans, i - first[ch] - 1].max
    else
      first[ch] = i
    end
  end
  ans
end
