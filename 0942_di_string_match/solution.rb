# LeetCode 0942 - DI String Match
# https://leetcode.com/problems/di-string-match/

# @param {String} s
# @return {Integer[]}
def di_string_match(s)
  lo = 0
  hi = s.length
  ans = []
  s.each_char do |ch|
    if ch == "I"
      ans << lo
      lo += 1
    else
      ans << hi
      hi -= 1
    end
  end
  ans << lo
  ans
end
