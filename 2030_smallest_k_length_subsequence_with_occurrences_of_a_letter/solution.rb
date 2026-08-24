# LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
# https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

# @param {String} s
# @param {Integer} k
# @param {Character} letter
# @param {Integer} repetition
# @return {String}
def smallest_subsequence(s, k, letter, repetition)
  n = s.length
  remain_letter = s.chars.count(letter)
  stack = []
  in_stack_letter = 0
  s.each_char.with_index do |ch, i|
    while !stack.empty? && ch < stack[-1] && stack.length + n - i > k
      top = stack[-1]
      if top == letter
        break if in_stack_letter + remain_letter - 1 < repetition

        in_stack_letter -= 1
      end
      stack.pop
    end
    if stack.length < k
      if ch == letter
        stack << ch
        in_stack_letter += 1
      elsif k - stack.length > repetition - in_stack_letter
        stack << ch
      end
    end
    remain_letter -= 1 if ch == letter
  end
  stack.join
end
