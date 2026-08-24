# LeetCode 2117 - Abbreviating the Product of a Range
# https://leetcode.com/problems/abbreviating-the-product-of-a-range/

# @param {Integer} left
# @param {Integer} right
# @return {String}
def abbreviate_product(left, right)
  prod = 1
  (left..right).each { |i| prod *= i }
  zeros = 0
  while prod % 10 == 0
    prod /= 10
    zeros += 1
  end
  s = prod.to_s
  return "#{s}e#{zeros}" if s.length <= 10

  "#{s[0, 5]}e#{zeros}#{s[-5, 5]}"
end
