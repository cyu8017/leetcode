# LeetCode 1784 - Check if Binary String Has at Most One Segment of Ones
# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

# @param {String} s
# @return {Boolean}
def check_ones_segment(s)
  trimmed = s.gsub(/\A0+|0+\z/, '')
  !trimmed.include?('01')
end
