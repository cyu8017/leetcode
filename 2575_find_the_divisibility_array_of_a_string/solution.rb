# LeetCode 2575 - Find the Divisibility Array of a String
# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

# @param {String} word
# @param {Integer} m
# @return {Integer[]}
def divisibility_array(word, m)
  ans = Array.new(word.length, 0)
  cur = 0
  word.each_char.with_index do |ch, i|
    cur = (cur * 10 + (ch.ord - 48)) % m
    ans[i] = 1 if cur == 0
  end
  ans
end
