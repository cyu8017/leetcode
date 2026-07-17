# LeetCode 1736 - Latest Time by Replacing Hidden Digits
# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

# @param {String} time
# @return {String}
def maximum_time(time)
  chars = time.chars
  chars[0] = "0123?".include?(chars[1]) ? "2" : "1" if chars[0] == "?"
  chars[1] = chars[0] == "2" ? "3" : "9" if chars[1] == "?"
  chars[3] = "5" if chars[3] == "?"
  chars[4] = "9" if chars[4] == "?"
  chars.join
end
