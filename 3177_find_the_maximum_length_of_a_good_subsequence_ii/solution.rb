# LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_length(nums, k)
  n = nums.length
  f = Array.new(n) { Array.new(k + 1, 0) }
  mp = Array.new(k + 1) { {} }
  g = Array.new(k + 1) { [0, 0, 0] }
  ans = 0
  (0...n).each do |i|
    (0..k).each do |h|
      f[i][h] = mp[h].fetch(nums[i], 0)
      if h > 0
        if g[h - 1][0] != nums[i]
          f[i][h] = [f[i][h], g[h - 1][1]].max
        else
          f[i][h] = [f[i][h], g[h - 1][2]].max
        end
      end
      f[i][h] += 1
      mp[h][nums[i]] = [mp[h].fetch(nums[i], 0), f[i][h]].max
      if g[h][0] != nums[i]
        if f[i][h] >= g[h][1]
          g[h][2] = g[h][1]
          g[h][1] = f[i][h]
          g[h][0] = nums[i]
        elsif f[i][h] > g[h][2]
          g[h][2] = f[i][h]
        end
      elsif f[i][h] > g[h][1]
        g[h][1] = f[i][h]
      end
      ans = [ans, f[i][h]].max
    end
  end
  ans
end
