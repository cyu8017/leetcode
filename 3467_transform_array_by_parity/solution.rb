# LeetCode 3467 - Transform Array by Parity
# https://leetcode.com/problems/transform-array-by-parity/

# @param {Integer[]} nums
# @return {Integer[]}
def transform_array(nums)
  (0...nums.length).each { |i| nums[i] %= 2 }
  j = 0
  (0...nums.length).each do |i|
    if nums[i] == 0
      nums[i], nums[j] = nums[j], nums[i]
      j += 1
    end
  end
  nums
end
