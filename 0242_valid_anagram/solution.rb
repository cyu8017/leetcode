# LeetCode 0242 - Valid Anagram
# https://leetcode.com/problems/valid-anagram/

# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
  return false if s.length != t.length

  counts = Array.new(26, 0)
  s.each_char.with_index do |left, index|
    counts[left.ord - 'a'.ord] += 1
    counts[t[index].ord - 'a'.ord] -= 1
  end
  counts.all?(&:zero?)
end
