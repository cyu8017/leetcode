# LeetCode 3992 - Rearrange String to Avoid Character Pair
# https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

# @param {String} s
# @param {String} x
# @param {String} y
# @return {String}
def rearrange_string(s, x, y)
  arr = s.chars
  i = 0
  arr.each_index do |j|
    if arr[j] == y
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
    end
  end
  arr.join
end
