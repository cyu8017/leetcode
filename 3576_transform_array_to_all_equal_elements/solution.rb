# LeetCode 3576 - Transform Array to All Equal Elements
# https://leetcode.com/problems/transform-array-to-all-equal-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def can_make_equal(nums, k)
  check = lambda do |arr, target, kk|
    cnt = 0
    sign = 1
    (0...(arr.length - 1)).each do |i|
      x = arr[i] * sign
      if x == target
        sign = 1
      else
        sign = -1
        cnt += 1
      end
    end
    cnt <= kk && arr[-1] * sign == target
  end
  check.call(nums, nums[0], k) || check.call(nums, -nums[0], k)
end
