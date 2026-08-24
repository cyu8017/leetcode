# LeetCode 2222 - Number of Ways to Select Buildings
# https://leetcode.com/problems/number-of-ways-to-select-buildings/

# @param {String} s
# @return {Integer}
def number_of_ways(s)
  total0 = s.count("0")
  total1 = s.length - total0
  left0 = left1 = ans = 0
  s.each_char do |c|
    if c == "0"
      ans += left1 * (total1 - left1)
      left0 += 1
    else
      ans += left0 * (total0 - left0)
      left1 += 1
    end
  end
  ans
end
