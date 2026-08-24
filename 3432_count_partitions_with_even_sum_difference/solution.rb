# LeetCode 3432 - Count Partitions with Even Sum Difference
# https://leetcode.com/problems/count-partitions-with-even-sum-difference/

# @param {Integer[]} nums
# @return {Integer}
def count_partitions(nums)
  total = 0
  nums.each { |x| total += x }
  ans = 0
  left = 0
  (0...(nums.length - 1)).each do |i|
    left += nums[i]
    ans += 1 if (left - (total - left)) % 2 == 0
  end
  ans
end
