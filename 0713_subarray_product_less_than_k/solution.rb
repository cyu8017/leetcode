# LeetCode 0713 - Subarray Product Less Than K
# https://leetcode.com/problems/subarray-product-less-than-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def num_subarray_product_less_than_k(nums, k)
  return 0 if k <= 1

  product = 1
  left = 0
  ans = 0
  nums.each_with_index do |num, right|
    product *= num
    while product >= k
      product /= nums[left]
      left += 1
    end
    ans += right - left + 1
  end
  ans
end
