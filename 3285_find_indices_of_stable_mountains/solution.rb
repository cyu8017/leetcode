# LeetCode 3285 - Find Indices of Stable Mountains
# https://leetcode.com/problems/find-indices-of-stable-mountains/

# @param {Integer[]} height
# @param {Integer} threshold
# @return {Integer[]}
def stable_mountains(height, threshold)
  ans = []
  (1...height.length).each do |i|
    ans << i if height[i - 1] > threshold
  end
  ans
end
