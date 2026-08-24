# LeetCode 2090 - K Radius Subarray Averages
# https://leetcode.com/problems/k-radius-subarray-averages/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def get_averages(nums, k)
  n = nums.length
  ans = Array.new(n, -1)
  return ans if 2 * k + 1 > n

  window = 2 * k + 1
  s = nums[0...window].sum
  ans[k] = s / window
  (k + 1).upto(n - k - 1) do |i|
    s += nums[i + k] - nums[i - k - 1]
    ans[i] = s / window
  end
  ans
end
