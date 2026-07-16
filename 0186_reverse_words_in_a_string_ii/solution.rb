# LeetCode 0186 - Reverse Words in a String II
# https://leetcode.com/problems/reverse-words-in-a-string-ii/

# @param {Character[]} s
# @return {void}
def reverse_words(s)
  reverse_range(s, 0, s.length - 1)
  start = 0

  (0..s.length).each do |finish|
    if finish == s.length || s[finish] == " "
      reverse_range(s, start, finish - 1)
      start = finish + 1
    end
  end
end

def reverse_range(chars, left, right)
  while left < right
    chars[left], chars[right] = chars[right], chars[left]
    left += 1
    right -= 1
  end
end