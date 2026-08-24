# LeetCode 3599 - Partition Array to Minimize XOR
# https://leetcode.com/problems/partition-array-to-minimize-xor/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_xor(nums, k)
  n = nums.length
  g = Array.new(n + 1, 0)
  (1..n).each { |i| g[i] = g[i - 1] ^ nums[i - 1] }
  inf = 2147483647 / 2
  f = Array.new(n + 1) { Array.new(k + 1, inf) }
  f[0][0] = 0
  (1..n).each do |i|
    (1..[i, k].min).each do |j|
      ((j - 1)...i).each do |h|
        f[i][j] = [f[i][j], [f[h][j - 1], g[i] ^ g[h]].max].min
      end
    end
  end
  f[n][k]
end
