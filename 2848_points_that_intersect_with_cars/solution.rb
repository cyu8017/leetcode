# LeetCode 2848 - Points That Intersect With Cars
# https://leetcode.com/problems/points-that-intersect-with-cars/

# @param {Integer[][]} nums
# @return {Integer}
def number_of_points(nums)
  cov = Array.new(102, 0)
  nums.each do |a, b|
    (a..b).each { |x| cov[x] = 1 }
  end
  cov.sum
end
