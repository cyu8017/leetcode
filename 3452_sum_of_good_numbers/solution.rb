# LeetCode 3452 - Sum of Good Numbers
# https://leetcode.com/problems/sum-of-good-numbers/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_of_good_numbers(nums, k)
  ans = 0
  n = nums.length
  (0...n).each do |i|
    x = nums[i]
    good = true
    good = false if i - k >= 0 && x <= nums[i - k]
    good = false if i + k < n && x <= nums[i + k]
    ans += x if good
  end
  ans
end
