# LeetCode 2495 - Number of Subarrays Having Even Product
# https://leetcode.com/problems/number-of-subarrays-having-even-product/

# @param {Integer[]} nums
# @return {Integer}
def even_product(nums)
  n = nums.length
  total = n * (n + 1) / 2
  odd_len = 0
  odd = 0
  nums.each do |x|
    if x.odd?
      odd += 1
      odd_len += odd
    else
      odd = 0
    end
  end
  total - odd_len
end
