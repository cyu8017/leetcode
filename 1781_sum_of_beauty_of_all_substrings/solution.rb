# LeetCode 1781 - Sum of Beauty of All Substrings
# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

# @param {String} s
# @return {Integer}
def beauty_sum(s)
  ans = 0
  bytes = s.bytes
  (0...bytes.length).each do |i|
    freq = Array.new(26, 0)
    (i...bytes.length).each do |j|
      freq[bytes[j] - 97] += 1
      nonzero = freq.reject(&:zero?)
      ans += nonzero.max - nonzero.min
    end
  end
  ans
end
