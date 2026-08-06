# LeetCode 1276 - Number of Burgers with No Waste of Ingredients
# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

# @param {Integer} tomato_slices
# @param {Integer} cheese_slices
# @return {Integer[]}
def num_of_burgers(tomato_slices, cheese_slices)
  jumbo = tomato_slices / 2 - cheese_slices
  small = cheese_slices - jumbo
  tomato_slices.even? && jumbo >= 0 && small >= 0 ? [jumbo, small] : []
end
