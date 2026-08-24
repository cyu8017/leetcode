# LeetCode 2875 - Minimum Size Subarray in Infinite Array
# https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def min_size_subarray(nums, target)
  n = nums.length
  total = nums.sum
  ans = 1 << 30
  if total > 0
    loops = target / total
    remain = target % total
    return loops * n if remain == 0

    arr = nums + nums
    left = 0
    s = 0
    best = 1 << 30
    (0...arr.length).each do |right|
      s += arr[right]
      while s > remain && left <= right
        s -= arr[left]
        left += 1
      end
      best = right - left + 1 if s == remain && right - left + 1 < best
    end
    ans = loops * n + best if best < (1 << 30)
  end
  ans == (1 << 30) ? -1 : ans
end
