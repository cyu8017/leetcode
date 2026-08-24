# LeetCode 3277 - Maximum XOR Score Subarray Queries
# https://leetcode.com/problems/maximum-xor-score-subarray-queries/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def maximum_subarray_xor(nums, queries)
  n = nums.length
  f = Array.new(n) { Array.new(n, 0) }
  (0...n).each { |i| f[i][i] = nums[i] }
  (2..n).each do |length|
    (0...(n - length + 1)).each do |i|
      j = i + length - 1
      f[i][j] = f[i][j - 1] ^ f[i + 1][j]
    end
  end
  best = Array.new(n) { Array.new(n, 0) }
  (0...n).each { |i| best[i][i] = f[i][i] }
  (2..n).each do |length|
    (0...(n - length + 1)).each do |i|
      j = i + length - 1
      best[i][j] = [f[i][j], best[i][j - 1], best[i + 1][j]].max
    end
  end
  queries.map { |q| best[q[0]][q[1]] }
end
