# LeetCode 2496 - Maximum Value of a String in an Array
# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

# @param {String[]} strs
# @return {Integer}
def maximum_value(strs)
  ans = 0
  strs.each do |s|
    all_digit = true
    val = 0
    s.each_char do |c|
      if c < "0" || c > "9"
        all_digit = false
        break
      end
      val = val * 10 + (c.ord - 48)
    end
    val = s.length unless all_digit
    ans = val if val > ans
  end
  ans
end
