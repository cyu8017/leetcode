# LeetCode 3069 - Distribute Elements Into Two Arrays I
# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

# @param {Integer[]} nums
# @return {Integer[]}
def result_array(nums)
  arr1 = [nums[0]]
  arr2 = [nums[1]]
  (2...nums.length).each do |i|
    if arr1[-1] > arr2[-1]
      arr1 << nums[i]
    else
      arr2 << nums[i]
    end
  end
  arr1 + arr2
end
