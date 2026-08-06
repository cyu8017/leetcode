# LeetCode 1153 - String Transforms Into Another String
# https://leetcode.com/problems/string-transforms-into-another-string/

# @param {String} str1
# @param {String} str2
# @return {Boolean}
def can_convert(str1, str2)
  return true if str1 == str2
  mapping = {}
  str1.chars.zip(str2.chars).each do |a, b|
    return false if mapping.key?(a) && mapping[a] != b
    mapping[a] = b
  end
  str2.chars.uniq.length < 26
end
