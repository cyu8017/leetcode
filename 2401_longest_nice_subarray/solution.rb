# LeetCode 2401 - Longest Nice Subarray
# https://leetcode.com/problems/longest-nice-subarray/

# @param {Integer[]} nums
# @return {Integer}
def longest_nice_subarray(nums)
  used = 0
  left = 0
  ans = 0
  nums.each_index do |right|
    while (used & nums[right]) != 0
      used ^= nums[left]
      left += 1
    end
    used |= nums[right]
    cand = right - left + 1
    ans = cand if cand > ans
  end
  ans
end
