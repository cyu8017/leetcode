# LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
  mx = nums.max
  ans = 0
  cnt = 0
  left = 0
  nums.each_with_index do |v, right|
    cnt += 1 if v == mx
    while cnt >= k
      cnt -= 1 if nums[left] == mx
      left += 1
    end
    ans += left
  end
  ans
end
