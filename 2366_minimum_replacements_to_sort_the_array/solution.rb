# LeetCode 2366 - Minimum Replacements to Sort the Array
# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

# @param {Integer[]} nums
# @return {Integer}
def minimum_replacement(nums)
  ans = 0
  n = nums.length
  prev = nums[n - 1]
  (n - 2).downto(0) do |i|
    if nums[i] <= prev
      prev = nums[i]
      next
    end
    parts = (nums[i] + prev - 1) / prev
    ans += parts - 1
    prev = nums[i] / parts
  end
  ans
end
