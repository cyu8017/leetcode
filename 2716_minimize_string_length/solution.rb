# LeetCode 2716 - Minimize String Length
# https://leetcode.com/problems/minimize-string-length/

# @param {String} s
# @return {Integer}
def minimized_string_length(s)
  s.chars.uniq.length
end
