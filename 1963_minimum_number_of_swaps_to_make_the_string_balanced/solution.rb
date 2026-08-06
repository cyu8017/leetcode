# LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

# @param {String} s
# @return {Integer}
def min_swaps(s)
  bal = 0
  mx = 0
  s.each_char do |ch|
    bal += ch == "[" ? 1 : -1
    mx = [mx, bal].min
  end
  (-mx + 1) / 2
end
