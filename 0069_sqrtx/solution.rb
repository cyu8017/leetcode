# LeetCode 0069 - Sqrt(x)
# https://leetcode.com/problems/sqrtx/

# @param {Integer} x
# @return {Integer}
def my_sqrt(x)
  return x if x < 2

  left = 2
  right = x / 2

  while left <= right
    mid = (left + right) / 2
    square = mid * mid
    return mid if square == x
    if square < x
      left = mid + 1
    else
      right = mid - 1
    end
  end

  right
end
