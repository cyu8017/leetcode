# LeetCode 2865 - Beautiful Towers I
# https://leetcode.com/problems/beautiful-towers-i/

# @param {Integer[]} heights
# @return {Integer}
def maximum_sum_of_heights(heights)
  n = heights.length
  ans = 0
  (0...n).each do |peak|
    s = heights[peak]
    mn = heights[peak]
    (peak - 1).downto(0) do |i|
      mn = heights[i] if heights[i] < mn
      s += mn
    end
    mn = heights[peak]
    (peak + 1...n).each do |i|
      mn = heights[i] if heights[i] < mn
      s += mn
    end
    ans = s if s > ans
  end
  ans
end
