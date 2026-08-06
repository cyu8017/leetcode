# LeetCode 1247 - Minimum Swaps to Make Strings Equal
# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

# @param {String} s1
# @param {String} s2
# @return {Integer}
def minimum_swap(s1, s2)
  xy = yx = 0
  s1.chars.zip(s2.chars).each do |a, b|
    xy += 1 if a == "x" && b == "y"
    yx += 1 if a == "y" && b == "x"
  end
  return -1 if (xy + yx).odd?
  xy / 2 + yx / 2 + 2 * (xy % 2)
end
