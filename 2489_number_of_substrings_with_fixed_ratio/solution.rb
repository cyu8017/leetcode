# LeetCode 2489 - Number of Substrings With Fixed Ratio
# https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

# @param {String} s
# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def fixed_ratio(s, num1, num2)
  pref = Hash.new(0)
  pref[0] = 1
  zeros = ones = ans = 0
  s.each_char do |c|
    if c == "0"
      zeros += 1
    else
      ones += 1
    end
    key = zeros * num2 - ones * num1
    ans += pref[key]
    pref[key] += 1
  end
  ans
end
