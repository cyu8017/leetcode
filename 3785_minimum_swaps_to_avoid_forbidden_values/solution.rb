# LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
# https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

# @param {Integer[]} nums
# @param {Integer[]} forbidden
# @return {Integer}
def min_swaps(nums, forbidden)
  n = nums.length
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  forbidden.each { |x| freq[x] += 1 }
  freq.each_value { |c| return -1 if c > n }
  bad = Hash.new(0)
  total = 0
  largest = 0
  (0...n).each do |i|
    next unless nums[i] == forbidden[i]
    bad[nums[i]] += 1
    total += 1
    largest = bad[nums[i]] if bad[nums[i]] > largest
  end
  return (total + 1) / 2 if (total + 1) / 2 > largest
  largest
end
