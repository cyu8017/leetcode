# LeetCode 3799 - Word Squares II
# https://leetcode.com/problems/word-squares-ii/

# @param {String[]} words
# @return {String[][]}
def word_squares(words)
  words = words.sort
  n = words.length
  ans = []
  (0...n).each do |i|
    top = words[i]
    (0...n).each do |j|
      next if j == i
      left = words[j]
      (0...n).each do |k|
        next if k == j || k == i
        right = words[k]
        (0...n).each do |h|
          next if h == k || h == j || h == i
          bottom = words[h]
          if top[0] == left[0] && top[3] == right[0] &&
             bottom[0] == left[3] && bottom[3] == right[3]
            ans << [top, left, right, bottom]
          end
        end
      end
    end
  end
  ans
end
