# LeetCode 1324 - Print Words Vertically
# https://leetcode.com/problems/print-words-vertically/

def print_vertically(s)
  words = s.split
  max_len = words.map(&:length).max
  (0...max_len).map do |i|
    words.map { |word| i < word.length ? word[i] : ' ' }.join.rstrip
  end
end
