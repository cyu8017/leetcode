# LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
# https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

# @param {Integer} d
# @param {Integer[]} nums
# @param {Integer} n
# @return {Boolean}
def adj_diff_ok(d, nums, n)
  prev = -1
  i = 0
  while i < n
    if nums[i] != -1
      return false if prev != -1 && (nums[i] - prev).abs > d

      prev = nums[i]
      i += 1
      next
    end
    j = i
    j += 1 while j < n && nums[j] == -1
    left = prev
    right = j < n ? nums[j] : -1
    gap = j - i
    return true if left == -1 && right == -1

    if left == -1 || right == -1
      prev = -1
      i = j
      next
    end
    return false if (left - right).abs > d * (gap + 1)

    prev = -1
    i = j
  end
  true
end

# @param {Integer[]} nums
# @return {Integer}
def min_difference(nums)
  n = nums.length
  lo = 0
  hi = 1_000_000_000
  while lo < hi
    mid = (lo + hi) / 2
    if adj_diff_ok(mid, nums, n)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
