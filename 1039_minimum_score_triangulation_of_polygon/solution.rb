# LeetCode 1039 - Minimum Score Triangulation of Polygon
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

# @param {Integer[]} values
# @return {Integer}
def min_score_triangulation(values)
  memo = {}
  dp = lambda do |i, j|
    return 0 if j - i < 2

    key = [i, j]
    return memo[key] if memo.key?(key)

    best = Float::INFINITY
    ((i + 1)...j).each do |k|
      best = [best, dp.call(i, k) + values[i] * values[k] * values[j] + dp.call(k, j)].min
    end
    memo[key] = best
  end
  dp.call(0, values.length - 1)
end
