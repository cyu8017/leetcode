# LeetCode 0028 - Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# @param {String} haystack
# @param {String} needle
# @return {Integer}
def str_str(haystack, needle)
  return 0 if needle.empty?

  needle_len = needle.length
  (0..haystack.length - needle_len).each do |i|
    return i if haystack[i, needle_len] == needle
  end
  -1
end
