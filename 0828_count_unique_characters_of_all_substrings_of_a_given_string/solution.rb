# LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

# @param {String} s
# @return {Integer}
def unique_letter_string(s)
  n = s.length
  last = {}
  s.each_char { |ch| last[ch] ||= [-1] }
  s.each_char.with_index { |ch, i| last[ch] << i }
  last.each_value { |indices| indices << n }
  ans = 0
  last.each_value do |indices|
    (1...indices.length - 1).each do |k|
      ans += (indices[k] - indices[k - 1]) * (indices[k + 1] - indices[k])
    end
  end
  ans
end
