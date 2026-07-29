# LeetCode 1014 - Best Sightseeing Pair
# https://leetcode.com/problems/best-sightseeing-pair/

# @param {Integer[]} values
# @return {Integer}
def max_score_sightseeing_pair(values)
  best = values[0]
  ans = 0
  (1...values.length).each do |j|
    ans = [ans, best + values[j] - j].max
    best = [best, values[j] + j].max
  end
  ans
end
