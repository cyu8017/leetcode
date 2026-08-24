# LeetCode 2710 - Remove Trailing Zeros From a String
# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

# @param {String} num
# @return {String}
def remove_trailing_zeros(num)
  last = num.length - 1
  last -= 1 while last >= 0 && num[last] == "0"
  last < 0 ? "" : num[0..last]
end
