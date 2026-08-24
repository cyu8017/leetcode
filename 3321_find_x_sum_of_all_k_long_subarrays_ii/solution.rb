# LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def find_x_sum(nums, k, x)
  n = nums.length
  ans = Array.new(n - k + 1, 0)
  (0..(n - k)).each do |i|
    freq = {}
    (i...(i + k)).each { |j| freq[nums[j]] = (freq[nums[j]] || 0) + 1 }
    arr = freq.map { |key, val| [key, val] }
    arr.sort_by! { |a| [-a[1], -a[0]] }
    lim = [x, arr.length].min
    keep = {}
    lim.times { |t| keep[arr[t][0]] = true }
    s = 0
    (i...(i + k)).each { |j| s += nums[j] if keep[nums[j]] }
    ans[i] = s
  end
  ans
end
