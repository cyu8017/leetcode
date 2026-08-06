# LeetCode 1525 - Number of Good Ways to Split a String
# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

# @param {String} s
# @return {Integer}
def num_splits(s)
  right = Hash.new(0)
  s.each_char { |ch| right[ch] += 1 }
  left = {}
  answer = 0
  s[0...-1].each_char do |ch|
    left[ch] = true
    right[ch] -= 1
    right.delete(ch) if right[ch] == 0
    answer += 1 if left.length == right.length
  end
  answer
end
