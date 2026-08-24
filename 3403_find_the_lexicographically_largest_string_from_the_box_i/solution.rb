# LeetCode 3403 - Find the Lexicographically Largest String From the Box I
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

# @param {String} word
# @param {Integer} num_friends
# @return {String}
def answer_string(word, num_friends)
  return word if num_friends == 1

  n = word.length
  max_len = n - (num_friends - 1)
  ans = ""
  (0...n).each do |i|
    last = i + max_len
    last = n if last > n
    cand = word[i...last]
    ans = cand if cand > ans
  end
  ans
end
