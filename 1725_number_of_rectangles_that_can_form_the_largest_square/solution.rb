# LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

# @param {Integer[][]} rectangles
# @return {Integer}
def count_good_rectangles(rectangles)
  sides = rectangles.map { |a, b| [a, b].min }
  best = sides.max
  sides.count(best)
end
