# LeetCode 2420 - Find All Good Indices
# https://leetcode.com/problems/find-all-good-indices/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def good_indices(nums, k)
  n = nums.length
  dec = Array.new(n, 0)
  inc = Array.new(n, 0)
  dec[0] = 1
  (1...n).each do |i|
    dec[i] = nums[i] <= nums[i - 1] ? dec[i - 1] + 1 : 1
  end
  inc[n - 1] = 1
  (n - 2).downto(0) do |i|
    inc[i] = nums[i] <= nums[i + 1] ? inc[i + 1] + 1 : 1
  end
  ans = []
  k.upto(n - k - 1) do |i|
    ans << i if dec[i - 1] >= k && inc[i + 1] >= k
  end
  ans
end
