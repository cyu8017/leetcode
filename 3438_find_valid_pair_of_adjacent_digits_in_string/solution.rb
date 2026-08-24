# LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

# @param {String} s
# @return {String}
def find_valid_pair(s)
  freq = Array.new(10, 0)
  s.each_char { |c| freq[c.ord - 48] += 1 }
  (0...(s.length - 1)).each do |i|
    a = s[i].ord - 48
    b = s[i + 1].ord - 48
    return s[i, 2] if a != b && freq[a] == a && freq[b] == b
  end
  ""
end
