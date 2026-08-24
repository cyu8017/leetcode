# LeetCode 3202 - Find the Maximum Length of Valid Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_length(nums, k)
  f = Array.new(k) { Array.new(k, 0) }
  ans = 0
  nums.each do |raw|
    x = raw % k
    (0...k).each do |j|
      y = (j - x + k) % k
      f[x][y] = f[y][x] + 1
      ans = [ans, f[x][y]].max
    end
  end
  ans
end
