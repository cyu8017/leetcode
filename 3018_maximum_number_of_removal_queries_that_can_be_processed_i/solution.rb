# LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
# https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer}
def maximum_processable_queries(nums, queries)
  n = nums.length
  f = Array.new(n) { Array.new(n, 0) }
  m = queries.length
  n.times do |i|
    (n - 1).downto(i) do |j|
      if i > 0
        t = f[i - 1][j] < m && nums[i - 1] >= queries[f[i - 1][j]] ? 1 : 0
        f[i][j] = [f[i][j], f[i - 1][j] + t].max
      end
      if j + 1 < n
        t = f[i][j + 1] < m && nums[j + 1] >= queries[f[i][j + 1]] ? 1 : 0
        f[i][j] = [f[i][j], f[i][j + 1] + t].max
      end
      return m if f[i][j] == m
    end
  end
  ans = 0
  n.times do |i|
    t = f[i][i] < m && nums[i] >= queries[f[i][i]] ? 1 : 0
    ans = [ans, f[i][i] + t].max
  end
  ans
end

def solve(*args)
  maximum_processable_queries(*args)
end
