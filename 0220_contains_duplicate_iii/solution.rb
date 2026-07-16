# LeetCode 0220 - Contains Duplicate III
# https://leetcode.com/problems/contains-duplicate-iii/

# @param {Integer[]} nums
# @param {Integer} index_diff
# @param {Integer} value_diff
# @return {Boolean}
def contains_nearby_almost_duplicate(nums, index_diff, value_diff)
  return false if index_diff <= 0 || value_diff.negative?

  width = value_diff + 1
  buckets = {}

  bucket_id = lambda do |num|
    num >= 0 ? num / width : (num + 1) / width - 1
  end

  nums.each_with_index do |num, i|
    bucket = bucket_id.call(num)
    return true if buckets.key?(bucket)
    return true if buckets.key?(bucket - 1) && (num - buckets[bucket - 1]).abs <= value_diff
    return true if buckets.key?(bucket + 1) && (num - buckets[bucket + 1]).abs <= value_diff

    if buckets.length >= index_diff
      old = nums[i - index_diff]
      buckets.delete(bucket_id.call(old))
    end
    buckets[bucket] = num
  end
  false
end
