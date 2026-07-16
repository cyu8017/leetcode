# LeetCode 0091 - Decode Ways
# https://leetcode.com/problems/decode-ways/

# @param {String} s
# @return {Integer}
def num_decodings(s)
  return 0 if s.nil? || s.empty? || s[0] == '0'

  prev2 = 1
  prev1 = 1

  (1...s.length).each do |i|
    current = 0
    current += prev1 if s[i] != '0'
    two = s[(i - 1)..i].to_i
    current += prev2 if two >= 10 && two <= 26
    prev2 = prev1
    prev1 = current
  end

  prev1
end
