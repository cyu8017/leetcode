# LeetCode 1064 - Fixed Point
# https://leetcode.com/problems/fixed-point/

# @param {Integer[]} arr
# @return {Integer}
def fixed_point(arr)
  lo = 0
  hi = arr.length - 1
  ans = -1
  while lo <= hi
    mid = (lo + hi) / 2
    if arr[mid] == mid
      ans = mid
      hi = mid - 1
    elsif arr[mid] < mid
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  ans
end
