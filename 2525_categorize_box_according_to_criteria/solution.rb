# LeetCode 2525 - Categorize Box According to Criteria
# https://leetcode.com/problems/categorize-box-according-to-criteria/

# @param {Integer} length
# @param {Integer} width
# @param {Integer} height
# @param {Integer} mass
# @return {String}
def categorize_box(length, width, height, mass)
  bulky = length >= 10_000 || width >= 10_000 || height >= 10_000 ||
          length * width * height >= 1_000_000_000
  heavy = mass >= 100
  return "Both" if bulky && heavy
  return "Bulky" if bulky
  return "Heavy" if heavy

  "Neither"
end
