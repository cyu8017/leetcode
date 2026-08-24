# LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_length(nums, k)
  n = nums.length
  f = Array.new(n) { Array.new(k + 1, 0) }
  ans = 0
  (0...n).each do |i|
    (0..k).each do |h|
      (0...i).each do |j|
        if nums[i] == nums[j]
          f[i][h] = [f[i][h], f[j][h]].max
        elsif h > 0
          f[i][h] = [f[i][h], f[j][h - 1]].max
        end
      end
      f[i][h] += 1
    end
    ans = [ans, f[i][k]].max
  end
  ans
end
