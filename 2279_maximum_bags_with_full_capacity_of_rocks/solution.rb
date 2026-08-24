# LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

# @param {Integer[]} capacity
# @param {Integer[]} rocks
# @param {Integer} additional_rocks
# @return {Integer}
def maximum_bags(capacity, rocks, additional_rocks)
  need = capacity.zip(rocks).map { |c, r| c - r }.sort
  ans = 0
  need.each do |n|
    break if additional_rocks < n

    additional_rocks -= n
    ans += 1
  end
  ans
end
