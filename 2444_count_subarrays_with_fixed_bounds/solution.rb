# LeetCode 2444 - Count Subarrays With Fixed Bounds
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

# @param {Integer[]} nums
# @param {Integer} min_k
# @param {Integer} max_k
# @return {Integer}
def count_subarrays(nums, min_k, max_k)
  ans = 0
  imin = imax = ibad = -1
  nums.each_with_index do |x, i|
    ibad = i if x < min_k || x > max_k
    imin = i if x == min_k
    imax = i if x == max_k
    bound = imin < imax ? imin : imax
    ans += bound - ibad if bound > ibad
  end
  ans
end
