# LeetCode 2262 - Total Appeal of A String
# https://leetcode.com/problems/total-appeal-of-a-string/

# @param {String} s
# @return {Integer}
def appeal_sum(s)
  last = Array.new(26, -1)
  ans = cur = 0
  s.chars.each_with_index do |ch, i|
    c = ch.ord - 97
    cur += i - last[c]
    last[c] = i
    ans += cur
  end
  ans
end
