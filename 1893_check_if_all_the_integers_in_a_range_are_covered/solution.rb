# LeetCode 1893 - Check if All the Integers in a Range Are Covered
# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

# @param {Integer[][]} ranges
# @param {Integer} left
# @param {Integer} right
# @return {Boolean}
def is_covered(ranges, left, right)
  covered = Array.new(51, false)
  ranges.each do |start, ending|
    (start..ending).each { |value| covered[value] = true }
  end
  (left..right).all? { |value| covered[value] }
end
