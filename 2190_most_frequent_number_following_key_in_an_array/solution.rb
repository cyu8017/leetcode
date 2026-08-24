# LeetCode 2190 - Most Frequent Number Following Key In an Array
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

# @param {Integer[]} nums
# @param {Integer} key
# @return {Integer}
def most_frequent(nums, key)
  freq = Hash.new(0)
  best = 0
  ans = 0
  i = 0
  while i + 1 < nums.length
    if nums[i] == key
      v = freq[nums[i + 1]] + 1
      freq[nums[i + 1]] = v
      if v > best
        best = v
        ans = nums[i + 1]
      end
    end
    i += 1
  end
  ans
end
