# LeetCode 1702 - Maximum Binary String After Change
# https://leetcode.com/problems/maximum-binary-string-after-change/

# @param {String} binary
# @return {String}
def maximum_binary_string(binary)
  zeros = binary.count("0")
  return binary if zeros <= 1
  first = binary.index("0")
  n = binary.length
  "1" * (first + zeros - 1) + "0" + "1" * (n - first - zeros)
end
