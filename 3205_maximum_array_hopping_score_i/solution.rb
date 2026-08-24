# LeetCode 3205 - Maximum Array Hopping Score I
# https://leetcode.com/problems/maximum-array-hopping-score-i/

# @param {Integer[]} nums
# @return {Integer}
def max_score(nums)
  n = nums.length
  f = Array.new(n, 0)
  dfs = lambda do |i|
    return f[i] if f[i] > 0
    ((i + 1)...n).each do |j|
      f[i] = [f[i], (j - i) * nums[j] + dfs.call(j)].max
    end
    f[i]
  end
  dfs.call(0)
end
