# LeetCode 0011 - Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

# @param {Integer[]} height
# @return {Integer}
def max_area(height)
  left = 0
  right = height.length - 1
  best = 0

  while left < right
    width = right - left
    best = [best, [height[left], height[right]].min * width].max
    if height[left] < height[right]
      left += 1
    else
      right -= 1
    end
  end

  best
end
