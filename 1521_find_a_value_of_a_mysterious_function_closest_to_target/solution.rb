# LeetCode 1521 - Find a Value of a Mysterious Function Closest to Target
# https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

require 'set'

# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def closest_to_target(arr, target)
  answer = Float::INFINITY
  current = Set.new
  arr.each do |value|
    current = Set[value] | current.map { |previous| value & previous }.to_set
    answer = [answer, current.map { |c| (c - target).abs }.min].min
  end
  answer
end
