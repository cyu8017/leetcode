# LeetCode 0229 - Majority Element II
# https://leetcode.com/problems/majority-element-ii/

# @param {Integer[]} nums
# @return {Integer[]}
def majority_element(nums)
  candidate1 = nil
  candidate2 = nil
  count1 = 0
  count2 = 0

  nums.each do |num|
    if num == candidate1
      count1 += 1
    elsif num == candidate2
      count2 += 1
    elsif count1.zero?
      candidate1 = num
      count1 = 1
    elsif count2.zero?
      candidate2 = num
      count2 = 1
    else
      count1 -= 1
      count2 -= 1
    end
  end

  count1 = 0
  count2 = 0
  nums.each do |num|
    count1 += 1 if num == candidate1
    count2 += 1 if num == candidate2
  end

  threshold = nums.length / 3
  result = []
  result << candidate1 if count1 > threshold
  result << candidate2 if candidate2 != candidate1 && count2 > threshold
  result
end
