# LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
# https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  g = []
  nums.each do |x|
    l = 0
    r = g.length
    while l < r
      mid = (l + r) >> 1
      if g[mid] < x
        r = mid
      else
        l = mid + 1
      end
    end
    if l == g.length
      g << x
    else
      g[l] = x
    end
  end
  g.length
end
