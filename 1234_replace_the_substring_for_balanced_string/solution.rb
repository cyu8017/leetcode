# LeetCode 1234 - Replace the Substring for Balanced String
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/

# @param {String} s
# @return {Integer}
def balanced_string(s)
  count = Hash.new(0)
  s.each_char { |ch| count[ch] += 1 }
  limit = s.length / 4
  n = s.length
  left = 0
  answer = n
  s.each_char.with_index do |ch, right|
    count[ch] -= 1
    while left < n && "QWER".chars.all? { |c| count[c] <= limit }
      answer = [answer, right - left + 1].min
      count[s[left]] += 1
      left += 1
    end
  end
  answer
end
