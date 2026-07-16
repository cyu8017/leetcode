# LeetCode 0165 - Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/

class Solution
  def compare_version(version1, version2)
    first = version1.split(".").map(&:to_i)
    second = version2.split(".").map(&:to_i)
    [first.length, second.length].max.times do |index|
      a = first[index] || 0
      b = second[index] || 0
      return a < b ? -1 : 1 if a != b
    end
    0
  end
end