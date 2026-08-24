# LeetCode 3254 - Find the Power of K-Size Subarrays I
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def results_array(nums, k)
  n = nums.length
  ans = Array.new(n - k + 1, 0)
  (0...(n - k + 1)).each do |i|
    ok = true
    ((i + 1)...(i + k)).each do |j|
      if nums[j] != nums[j - 1] + 1
        ok = false
        break
      end
    end
    ans[i] = ok ? nums[i + k - 1] : -1
  end
  ans
end
