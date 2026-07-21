# LeetCode 1852 - Distinct Numbers in Each Subarray
# https://leetcode.com/problems/distinct-numbers-in-each-subarray/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def distinct_numbers(nums, k)
  counts = Hash.new(0)
  nums[0...k].each { |num| counts[num] += 1 }
  result = [counts.length]
  left = 0

  (k...nums.length).each do |right|
    counts[nums[right]] += 1
    outgoing = nums[left]
    counts[outgoing] -= 1
    counts.delete(outgoing) if counts[outgoing] == 0
    left += 1
    result << counts.length
  end

  result
end
