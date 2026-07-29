# LeetCode 1081 - Smallest Subsequence of Distinct Characters
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

# @param {String} s
# @return {String}
def smallest_subsequence(s)
  last = {}
  s.each_char.with_index { |ch, i| last[ch] = i }
  stack = []
  used = {}
  s.each_char.with_index do |ch, i|
    next if used[ch]

    while !stack.empty? && ch < stack[-1] && last[stack[-1]] > i
      used.delete(stack.pop)
    end
    stack << ch
    used[ch] = true
  end
  stack.join
end
