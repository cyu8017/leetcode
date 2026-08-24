# LeetCode 3210 - Find the Encrypted String
# https://leetcode.com/problems/find-the-encrypted-string/

# @param {String} s
# @param {Integer} k
# @return {String}
def get_encrypted_string(s, k)
  n = s.length
  out = []
  (0...n).each { |i| out << s[(i + k) % n] }
  out.join
end
