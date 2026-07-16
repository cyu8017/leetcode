# LeetCode 0263 - Ugly Number
# https://leetcode.com/problems/ugly-number/

# @param {Integer} n
# @return {Boolean}
def is_ugly(n)
  return false if n <= 0

  value = n
  [2, 3, 5].each do |factor|
    while value % factor == 0
      value /= factor
    end
  end
  value == 1
end
