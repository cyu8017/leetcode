# LeetCode 0151 - Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution
  def reverse_words(s)
    s.split.reverse.join(" ")
  end
end