# LeetCode 1256 - Encode Number
# https://leetcode.com/problems/encode-number/

# @param {Integer} num
# @return {String}
def encode(num)
  (num + 1).to_s(2)[1..] || ""
end
