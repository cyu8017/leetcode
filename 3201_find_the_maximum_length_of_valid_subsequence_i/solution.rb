# LeetCode 3201 - Find the Maximum Length of Valid Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

# @param {Integer[]} nums
# @return {Integer}
def maximum_length(nums)
  k = 2
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
