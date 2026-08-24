# LeetCode 3920 - Maximize Fixed Points After Deletions
# https://leetcode.com/problems/maximize-fixed-points-after-deletions/

# @param {Integer[]} nums
# @return {Integer}
def max_fixed_points(nums)
  tails = []
  nums.each_with_index do |val, i|
    next if i < val
    d = i - val
    lo = 0
    hi = tails.length
    while lo < hi
      mid = (lo + hi) >> 1
      if tails[mid] <= d
        lo = mid + 1
      else
        hi = mid
      end
    end
    if lo == tails.length
      tails << d
    else
      tails[lo] = d
    end
  end
  tails.length
end
