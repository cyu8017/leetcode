# LeetCode 2566 - Maximum Difference by Remapping a Digit
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

# @param {Integer} num
# @return {Integer}
def min_max_difference(num)
  s = num.to_s

  remap = lambda do |frm, to|
    v = 0
    s.each_char do |c|
      d = c == frm ? to : c
      v = v * 10 + (d.ord - 48)
    end
    v
  end

  max_v = num
  s.each_char do |c|
    if c != "9"
      max_v = remap.call(c, "9")
      break
    end
  end
  min_v = remap.call(s[0], "0")
  max_v - min_v
end
