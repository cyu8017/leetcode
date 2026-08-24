# LeetCode 3000 - Maximum Area of Longest Diagonal Rectangle
# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

# @param {Integer[][]} dimensions
# @return {Integer}
def area_of_max_diagonal(dimensions)
  ans = 0
  mx = 0
  dimensions.each do |d|
    l = d[0]
    w = d[1]
    t = l * l + w * w
    if mx < t
      mx = t
      ans = l * w
    elsif mx == t
      area = l * w
      ans = area if area > ans
    end
  end
  ans
end
