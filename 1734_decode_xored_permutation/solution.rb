# LeetCode 1734 - Decode XORed Permutation
# https://leetcode.com/problems/decode-xored-permutation/

# @param {Integer[]} encoded
# @return {Integer[]}
def decode(encoded)
  n = encoded.length + 1
  total = 0
  (1..n).each { |value| total ^= value }
  odd = 0
  (1...encoded.length).step(2) { |i| odd ^= encoded[i] }
  ans = [total ^ odd]
  encoded.each { |value| ans << (ans[-1] ^ value) }
  ans
end
