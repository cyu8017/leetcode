# LeetCode 3936 - Minimum Swaps To Move Zeros To End
# https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

# @param {Integer[]} nums
# @return {Integer}
def minimum_swaps(nums)
  ans = 0
  n = nums.length
  i = 0
  j = n - 1
  while i < j
    i += 1 while i < n && nums[i] != 0
    j -= 1 while j > 0 && nums[j] == 0
    break if i >= j
    ans += 1
    i += 1
    j -= 1
  end
  ans
end
