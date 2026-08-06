# LeetCode 1528 - Shuffle String
# https://leetcode.com/problems/shuffle-string/

# @param {String} s
# @param {Integer[]} indices
# @return {String}
def restore_string(s, indices)
  answer = Array.new(s.length)
  s.chars.each_with_index { |ch, i| answer[indices[i]] = ch }
  answer.join
end
