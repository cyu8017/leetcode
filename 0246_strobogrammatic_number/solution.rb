# LeetCode 0246 - Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/

# @param {String} num
# @return {Boolean}
def is_strobogrammatic(num)
  mapping = { "0" => "0", "1" => "1", "6" => "9", "8" => "8", "9" => "6" }
  left = 0
  right = num.length - 1
  while left <= right
    return false if mapping[num[left]] != num[right]

    left += 1
    right -= 1
  end
  true
end
