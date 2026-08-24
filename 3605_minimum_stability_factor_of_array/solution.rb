# LeetCode 3605 - Minimum Stability Factor of Array
# https://leetcode.com/problems/minimum-stability-factor-of-array/

# @param {Integer[]} nums
# @param {Integer} max_c
# @return {Integer}
def min_stable(nums, max_c)
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  ok = lambda do |arr, maxc, x|
    n = arr.length
    return true if x >= n
    changes = 0
    i = 0
    while i + x < n
      g = arr[i]
      ((i + 1)..(i + x)).each { |j| g = gcd.call(g, arr[j]) }
      if g > 1
        changes += 1
        i += x + 1
      else
        i += 1
      end
    end
    changes <= maxc
  end
  n = nums.length
  lo = 0
  hi = n
  while lo < hi
    mid = (lo + hi) / 2
    if ok.call(nums, max_c, mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
