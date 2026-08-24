# LeetCode 0926 - Flip String to Monotone Increasing
# https://leetcode.com/problems/flip-string-to-monotone-increasing/

# @param {String} s
# @return {Integer}
def min_flips_mono_incr(s)
  ones = 0
  ans = 0
  s.each_char do |ch|
    if ch == "1"
      ones += 1
    else
      ans = [ans + 1, ones].min
    end
  end
  ans
end
