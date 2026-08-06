# LeetCode 1299 - Replace Elements with Greatest Element on Right Side
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

# @param {Integer[]} arr
# @return {Integer[]}
def replace_elements(arr)
  greatest = -1
  (arr.length - 1).downto(0) do |i|
    arr[i], greatest = greatest, [greatest, arr[i]].max
  end
  arr
end
