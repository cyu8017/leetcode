# LeetCode 2898 - Maximum Linear Stock Score
# https://leetcode.com/problems/maximum-linear-stock-score/

# @param {Integer[]} prices
# @return {Integer}
def max_score(prices)
  best = {}
  ans = 0
  prices.each_with_index do |price, i|
    key = price - (i + 1)
    cand = best.fetch(key, 0) + price
    best[key] = cand if cand > best.fetch(key, 0)
    ans = best[key] if best[key] > ans
  end
  ans
end
