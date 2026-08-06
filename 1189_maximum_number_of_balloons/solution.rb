# LeetCode 1189 - Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/

# @param {String} text
# @return {Integer}
def max_number_of_balloons(text)
  count = Hash.new(0)
  text.each_char { |c| count[c] += 1 }
  [count["b"], count["a"], count["l"] / 2, count["o"] / 2, count["n"]].min
end
