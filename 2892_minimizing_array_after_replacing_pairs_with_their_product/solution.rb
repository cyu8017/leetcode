# LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
# https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_array_length(nums, k)
  return 0 if nums.empty?

  ans = 1
  prod = nums[0]
  (1...nums.length).each do |i|
    if prod <= k && nums[i] <= k && (nums[i] == 0 || prod <= k / nums[i])
      prod *= nums[i]
    else
      ans += 1
      prod = nums[i]
    end
  end
  ans
end
