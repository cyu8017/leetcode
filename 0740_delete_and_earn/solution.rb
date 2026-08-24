# LeetCode 0740 - Delete and Earn
# https://leetcode.com/problems/delete-and-earn/

# @param {Integer[]} nums
# @return {Integer}
def delete_and_earn(nums)
  return 0 if nums.empty?

  max_num = nums.max
  points = Array.new(max_num + 1, 0)
  nums.each { |num| points[num] += num }

  take = 0
  skip = 0
  points.each do |value|
    take, skip = skip + value, [skip, take].max
  end
  [take, skip].max
end
