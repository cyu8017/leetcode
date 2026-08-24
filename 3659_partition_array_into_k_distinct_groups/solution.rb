# LeetCode 3659 - Partition Array Into K-Distinct Groups
# https://leetcode.com/problems/partition-array-into-k-distinct-groups/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def partition_array(nums, k)
  n = nums.length
  return false if n % k != 0

  m = n / k
  mx = nums.max
  cnt = Array.new(mx + 1, 0)
  nums.each do |x|
    cnt[x] += 1
    return false if cnt[x] > m
  end
  true
end
