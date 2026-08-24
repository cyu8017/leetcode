# LeetCode 0698 - Partition to K Equal Sum Subsets
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def can_partition_k_subsets(nums, k)
  total = nums.sum
  return false if total % k != 0

  target = total / k
  nums = nums.sort.reverse
  return false if nums[0] > target

  buckets = Array.new(k, 0)
  dfs = lambda do |index|
    return true if index == nums.length

    k.times do |i|
      next if buckets[i] + nums[index] > target

      buckets[i] += nums[index]
      return true if dfs.call(index + 1)

      buckets[i] -= nums[index]
      break if buckets[i] == 0
    end
    false
  end

  dfs.call(0)
end
