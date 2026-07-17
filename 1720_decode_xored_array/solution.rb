# LeetCode 1720 - Decode XORed Array
# https://leetcode.com/problems/decode-xored-array/

# @param {Integer[]} encoded
# @param {Integer} first
# @return {Integer[]}
def decode(encoded, first)
  ans = [first]
  encoded.each { |value| ans << (ans[-1] ^ value) }
  ans
end
